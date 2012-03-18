from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django_contact_form.forms import ContactForm


def contact(request):
    recipients = getattr(settings, 'CONTACT_FORM_RECIPIENTS', settings.MANAGERS)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', cd['email']),
                [i[1] for i in recipients], # send to managers as defined in project's settings.py file
            )
            return HttpResponseRedirect(reverse('success'))
    else:
        form = ContactForm(
            #initial={'subject': 'Message from the contact form.'} # prepopulates the subject line
        )

    if request.is_ajax():
        return render_to_response('contact/form.html', {'form': form}, context_instance=RequestContext(request))
    else:
        return render_to_response('contact/contact_form.html', {'form': form}, context_instance=RequestContext(request))