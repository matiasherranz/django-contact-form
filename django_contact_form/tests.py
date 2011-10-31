from django.test import TestCase
from django.test.client import Client

class SimpleTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.post_dict = {'email': 'nobody@example.com', 
                          'subject': 'Test', 
                          'message': 'This is a test message.'}
    
    def test_form_url(self):
        # Issue a GET request.
        response = self.client.get('/contact/')
        
        # Check that the response is 200 OK.
        self.failUnlessEqual(response.status_code, 200)

        # Check that the correct template is being used.
        self.assertTemplateUsed(response, 'contact/contact_form.html')
        
        # Issue a POST request.
        response = self.client.post('/contact/', self.post_dict, follow=False)
        
        # Check that the response is 200 OK.
        self.failUnlessEqual(response.status_code, 302)

    def test_thanks_url(self):
        response = self.client.post('/contact/', self.post_dict, follow=True)

        # Check that the response is 200 OK.
        self.failUnlessEqual(response.status_code, 200)

        # Check that the correct template is being used.
        self.assertTemplateUsed(response, 'contact/thanks.html')
        
        # Check that the response is being properly routed.
        self.failUnlessEqual(response.redirect_chain, [('http://testserver/contact/thanks/', 302)])

    def test_subject_is_required(self):
        self.post_dict['subject'] = ''
        response = self.client.post('/contact/', self.post_dict)
        self.assertFormError(response, 'form', 'subject', [u'This field is required.'])
        
    def test_message_is_required(self):
        self.post_dict['message'] = ''
        response = self.client.post('/contact/', self.post_dict)
        self.assertFormError(response, 'form', 'message', [u'This field is required.'])
    
    def test_message_must_be_4_words_long(self):
        self.post_dict['message'] = 'one two three'
        response = self.client.post('/contact/', self.post_dict)
        self.assertFormError(response, 'form', 'message', [u'This must be at least 4 words in length.'])
    
    def test_email_address_is_required(self):
        self.post_dict['email'] = ''
        response = self.client.post('/contact/', self.post_dict)
        self.assertFormError(response, 'form', 'email', [u'This field is required.'])
        
    def test_email_adderss_is_valid(self):
        self.post_dict['email'] = 'nobody@example'
        response = self.client.post('/contact/', self.post_dict)
        self.assertFormError(response, 'form', 'email', [u'Enter a valid e-mail address.'])
