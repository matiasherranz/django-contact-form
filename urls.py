from django.conf.urls.defaults import *
from contact.views import contact

urlpatterns = patterns('',
    (r'^$', contact, {}, 'contact'),
    (r'^thanks/$', 'django.views.generic.simple.direct_to_template', { 'template': 'thanks.html' }),
)
