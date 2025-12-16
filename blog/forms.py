# blog/forms.py
from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(label='Twój e-mail', required=True)
    subject = forms.CharField(label='Temat', max_length=100, required=True)
    message = forms.CharField(label='Wiadomość', widget=forms.Textarea, required=True)
    full_name = forms.CharField(label='Imię i nazwisko', max_length=100, required=True)