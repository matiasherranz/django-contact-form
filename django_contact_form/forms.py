from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(label='Your email address')
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        """
        Simple custom validation example. Require 4+ words in the message field.
        
        Django's forms system automatically looks for any method whose name 
        starts with clean_ and ends with the name of the field. If any such 
        methods exist, they're called during validation.
        
        Specifically, clean_message() will be called after the default 
        validation logic for a given field.
        """
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("This must be at least 4 words in"\
                                        " length.")
        return message # Explicitly return the cleaned value at the end of the 
                       # message to allow us to modify the value within our 
                       # custom validation method. If we don't return it 
                       # explicitly, None will be returned and the original 
                       # value will be lost.