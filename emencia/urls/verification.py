# --- subscriber verification --- start ---------------------------------------
"""Urls for the emencia Subscriber Verification"""
from django.conf.urls import url, patterns

from emencia.forms \
    import SubscriberVerificationForm, VerificationMailingListSubscriptionForm

urlpatterns = patterns(
    'emencia.views.verification',
    url(
        r'^$',
        'view_subscriber_verification',
        {'form_class': SubscriberVerificationForm},
        name='newsletter_subscriber_verification',
    ),
    url(
        r'^(?P<link_id>[\w-]+)/$',
        'view_uuid_verification',
        {'form_class': VerificationMailingListSubscriptionForm},
        name='newsletter_subscriber_verification',
    ),
)

# --- subscriber verification --- end -----------------------------------------
