from django import forms

class ContactForm(forms.Form):
  contact_name = forms.CharField(max_length=100)
  contact_email = forms.EmailField()
  message_subject = forms.CharField(max_length=100)
  message_body = forms.CharField(widget=forms.Textarea)
  cc_myself = forms.BooleanField(required=False)