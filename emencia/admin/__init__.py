"""Admin for emencia"""
from django.contrib import admin
from django.conf import settings

from emencia.models import Link
from emencia.models import Contact
from emencia.models import WorkGroup
from emencia.models import SMTPServer
from emencia.models import Newsletter
from emencia.models import MailingList
from emencia.models import ContactMailingStatus

from emencia.settings import USE_WORKGROUPS
from emencia.admin.contact import ContactAdmin
from emencia.admin.workgroup import WorkGroupAdmin
from emencia.admin.newsletter import NewsletterAdmin
from emencia.admin.smtpserver import SMTPServerAdmin
from emencia.admin.mailinglist import MailingListAdmin


admin.site.register(Contact, ContactAdmin)
admin.site.register(SMTPServer, SMTPServerAdmin)
admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(MailingList, MailingListAdmin)

if USE_WORKGROUPS:
    admin.site.register(WorkGroup, WorkGroupAdmin)


class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'creation_date')

if settings.DEBUG:
    admin.site.register(Link, LinkAdmin)
    admin.site.register(ContactMailingStatus)
