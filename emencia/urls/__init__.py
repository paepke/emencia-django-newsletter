"""Default urls for the emencia"""
from django.conf.urls import url
from django.conf.urls import include
from django.conf.urls import patterns

urlpatterns = patterns('',
                       url(r'^mailing/', include('emencia.urls.mailing_list')),
                       url(r'^tracking/', include('emencia.urls.tracking')),
                       url(r'^statistics/', include('emencia.urls.statistics')),
                       url(r'^', include('emencia.urls.newsletter')),
                       )
