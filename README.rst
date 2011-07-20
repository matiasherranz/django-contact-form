=====================
 Django Contact Form
=====================

Installation from Source
========================

::

 $ git clone git@github.com:jbergantine/django-contact-form.git
 $ cd django-contact-form
 $ python setup.py install

Setup the Project For the Application
=====================================

Add to the project's settings.py file tuple of installed apps: ::

 'django_contact_form',

In the project's urls.py file add: ::

 url(r'^contact/', include('django_contact_form.urls')),

Setup the Recipients of the Contact Form
========================================

Form submissions will go to either a list of recipients defined in a custom tuple called CONTACT_FORM_RECIPIENTS or, if that can't be found in the settings file, the list of MANAGERS. The format for CONTACT_FORM_RECIPIENTS should follow the format for MANAGERS and should look something like: ::

 CONTACT_FORM_RECIPIENTS = (
     ('Barack Obama', 'barack@whitehouse.gov'),
 )

Configure Email Settings for Sending
====================================

In the project's settings.py file configure the following: ::

 EMAIL_HOST = ''
 EMAIL_HOST_USER = ''
 EMAIL_HOST_PASSWORD = ''
 DEFAULT_FROM_EMAIL = ''

Configure the Templates
=======================

By default the templates contain only the bare necessities. To override the default templates, create a directory called contact in your templates directory and add 2 files: contact_form.html and thanks.html. To copy the templates cd to the root of the django project and execute the following command: ::

 cp -r ../src/django-contact-form/django_contact_form/templates/contact templates/contact