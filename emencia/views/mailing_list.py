"""
Views for emencia Mailing List and Subscriber Verification
"""
import re

from django.template import Context, Template
from django.template import RequestContext
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404, render_to_response
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_str

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.encoders import encode_base64
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage

from emencia.models import Newsletter
from emencia.models import MailingList
from emencia.models import ContactMailingStatus
from emencia.models import SMTPServer
from emencia.models import SubscriberVerification
from emencia.settings import DEFAULT_HEADER_REPLY
from emencia.settings import UNSUBSCRIBE_ALL
from emencia.settings import AUTO_SUBSCRIBE_TO_ONLY_LIST
from emencia.settings import AUTO_SUBSCRIBE_LIST_NAME
from emencia.utils.tokens import untokenize

from StringIO import StringIO

from html2text import html2text as html2text_orig


def view_mailinglist_unsubscribe(request, slug, uidb36, token):
    """
    Unsubscribe a contact to one or all mailing lists
    """
    newsletter = get_object_or_404(Newsletter, slug=slug)
    contact = untokenize(uidb36, token)
    if UNSUBSCRIBE_ALL:
        mailing_lists = MailingList.objects.all()
        contact.subscriber = False
        contact.save()
    else:
        mailing_lists = [newsletter.mailing_list]

    unsubscribed = 0
    already_unsubscribed = False

    if request.POST.get('email'):
        for mailing_list in mailing_lists:
            already_unsubscribed = contact in mailing_list.unsubscribers.all()

            if not already_unsubscribed:
                mailing_list.unsubscribers.add(contact)
            unsubscribed += 1

    if unsubscribed > 0:
        already_unsubscribed = True
        ContactMailingStatus.objects.create(
            newsletter=newsletter,
            contact=contact,
            status=ContactMailingStatus.UNSUBSCRIPTION
        )

    return render_to_response(
        'newsletter/mailing_list_unsubscribe.html',
        {'email': contact.email, 'unsubscribed_count':unsubscribed, 'already_unsubscribed': already_unsubscribed},
        context_instance=RequestContext(request)
    )


def view_mailinglist_subscribe(request, form_class, mailing_list_id=None, link_id=None):
    """
    A simple view that shows a form for subscription for a mailing list(s).
    """
    subscribed = False
    mailing_list = None
    if mailing_list_id:
        mailing_list = get_object_or_404(MailingList, id=mailing_list_id)

    if request.POST and not subscribed:
        form = form_class(request.POST)
        if form.is_valid():
            form.save(mailing_list)
            subscribed = True
    else:
        form = form_class()

    return render_to_response(
        'newsletter/mailing_list_subscribe.html',
        {'subscribed': subscribed, 'mailing_list': mailing_list, 'form': form},
        context_instance=RequestContext(request)
    )

LINK_RE = re.compile(r"https?://([^ \n]+\n)+[^ \n]+", re.MULTILINE)


def html2text(html):
    """
    Use html2text but repair newlines cutting urls.
    Need to use this hack until https://github.com/aaronsw/html2text/issues/#issue/7 is not fixed
    """
    txt = html2text_orig(html)
    links = list(LINK_RE.finditer(txt))
    out = StringIO()
    pos = 0
    for l in links:
        out.write(txt[pos:l.start()])
        out.write(l.group().replace('\n', ''))
        pos = l.end()
    out.write(txt[pos:])
    return out.getvalue()


def view_subscriber_verification(request, form_class):
    """
    A simple view that shows a form for subscription for the newsletter.
    """
    context = {}

    if request.POST:
        context['form'] = form_class(request.POST)
        subscription = SubscriberVerification()
        if context['form'].is_valid():
            contact = context['form'].save()

            subscription.contact = context['form'].instance
            subscription.save()
            link_id = subscription.link_id

            server = SMTPServer.objects.get(id=1)  # TODO: Fix this assumption that the first smtp is id 1
            smtp = server.connect()

            message = _()
            from_mail = DEFAULT_HEADER_REPLY
            to_mail = context['form'].instance.email

            mail_context = Context({
                'base_url': "%s://%s" % ("https" if request.is_secure() else "http", request.get_host()),
                'link_id': link_id,
            })

            content_html = render_to_string('newsletter/newsletter_mail_verification.html', mail_context)

            content_text = html2text(content_html)

            message = MIMEMultipart()

            message['Subject'] = render_to_string('newsletter/newsletter_mail_verification_subject.html', context)
            message['From'] = smart_str(DEFAULT_HEADER_REPLY)
            message['Reply-to'] = smart_str(DEFAULT_HEADER_REPLY)
            message['To'] = smart_str(context['form'].instance.email)

            message_alt = MIMEMultipart('alternative')
            message_alt.attach(MIMEText(smart_str(content_text), 'plain', 'UTF-8'))
            message_alt.attach(MIMEText(smart_str(content_html), 'html', 'UTF-8'))
            message.attach(message_alt)

            try:
                smtp.sendmail(from_mail, to_mail, message.as_string())
            except Exception, e:
                print e
            smtp.quit()

            context['send'] = True

    else:
        context['form'] = form_class()

    return render_to_response(
        'newsletter/subscriber_verification.html',
        context,
        context_instance=RequestContext(request)
    )

def view_uuid_verification(request, link_id, form_class=None):
    """
    A simple view that shows if verification is true or false.
    """
    context = {}
    context['mailinglists'] = mailinglists = MailingList.objects.filter(public=True)
    context['mailing_list_count'] = mailinglists.count()
    context['link_id'] = link_id

    try:
        subscription = {}
        subscription['object'] = SubscriberVerification.objects.get(link_id=link_id)
        context['uuid_exist'] = True
        subscription['contact'] = subscription['object'].contact
        ready = True

        # If there is only one mailing list, subscribe the (now)
        # verified user to it
        if AUTO_SUBSCRIBE_TO_ONLY_LIST:
            if context['mailing_list_count'] == 1:
                mailing_list = mailinglists.get()
                mailing_list.subscribers.add(subscription['contact'].id)
                mailing_list.unsubscribers.remove(subscription['contact'].id)

        if AUTO_SUBSCRIBE_LIST_NAME is not None:
            if isinstance(AUTO_SUBSCRIBE_LIST_NAME, basestring):
                lists = [AUTO_SUBSCRIBE_LIST_NAME]
            else:
                lists = AUTO_SUBSCRIBE_LIST_NAME

            mls = mailinglists.filter(name__in=lists)
            for ml in mls:
                ml.subscribers.add(subscription['contact'].id)
                ml.unsubscribers.remove(subscription['contact'].id)

        if request.POST:
            form = form_class(request.POST)
            if form.is_valid():
                form.save(subscription['contact'].id)
                context['send'] = True
            else:
                ready = False
        else:
            context['form'] = form_class()

        if ready:
            subscription['contact'].verified = True
            subscription['contact'].save()
            subscription['object'].delete()

    except SubscriberVerification.DoesNotExist:
        context['uuid_exist'] = False

    return render_to_response(
        'newsletter/uuid_verification.html',
        context,
        context_instance=RequestContext(request)
    )
