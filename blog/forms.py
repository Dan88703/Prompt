from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class ContactForm(forms.Form):
    from_email = forms.EmailField(label='Twój e-mail', required=True)
    subject = forms.CharField(label='Temat', max_length=100, required=True)
    message = forms.CharField(
        label='Wiadomość',
        widget=forms.Textarea,
        required=True
    )
    full_name = forms.CharField(
        label='Imię i nazwisko',
        max_length=100,
        required=True
    )


class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        label="Nazwa użytkownika",
        max_length=150
    )
    email = forms.EmailField(
        label="Adres e-mail"
    )
    password1 = forms.CharField(
        label="Hasło",
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label="Powtórz hasło",
        widget=forms.PasswordInput
    )

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Hasła muszą być identyczne")

        if cleaned_data.get("username"):
            if User.objects.filter(username=cleaned_data["username"]).exists():
                raise ValidationError("Użytkownik o takiej nazwie już istnieje")

        return cleaned_data
