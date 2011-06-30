from django.conf.urls.defaults import *
from contact.views import contact

urlpatterns = patterns('',
    url(r'^$', contact, {}, 'contact'),
    url(r'^thanks/$', 'django.views.generic.simple.direct_to_template', { 'template': 'contact/thanks.html' }),
)
