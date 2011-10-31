from django.conf.urls.defaults import *
from django_contact_form.views import contact

urlpatterns = patterns('',
    url(r'^$', contact, {}, 'contact'),
    url(r'^thanks/$', 'django.views.generic.simple.direct_to_template', { 'template': 'contact/success.html' }, 'success'),
)
