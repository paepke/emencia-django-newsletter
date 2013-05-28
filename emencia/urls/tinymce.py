from django.conf.urls.defaults import url
from django.conf.urls.defaults import patterns


urlpatterns = patterns('emencia.views.tinymce_utils',
    url(r'^templates/$', 'view_tinymce_templates', name='tinymce_templates_list'),
)
