Installation from Source
========================

`git clone git@github.com:jbergantine/django-contact-form.git`
`cd django-contact-form`
`python setup.py install`

Setup the project for the application
-------------------------------------

Add to the project's settings.py file tuple of installed apps:
`'django_contact_form',`

In the project's urls.py file add:
`url(r'^contact/', include('django_contact_form.urls')),`

Setup the recipients of the contact form
----------------------------------------

Form submissions will go to either a list of recipients defined in a custom tuple called CONTACT_FORM_RECIPIENTS or, if that can't be found in the settings file, the list of MANAGERS. The format for CONTACT_FORM_RECIPIENTS should follow the format for MANAGERS and should look something like:
`CONTACT_FORM_RECIPIENTS = (
    ('Barack Obama', 'barack@whitehouse.gov'),
)`

Configure email settings for sending
------------------------------------

In the project's settings.py file configure the following:

`EMAIL_HOST = ''`
`EMAIL_HOST_USER = ''`
`EMAIL_HOST_PASSWORD = ''`
`DEFAULT_FROM_EMAIL = ''`

Configure the templates
-----------------------

By default the templates contain only the bare necessities.