from django import forms
from .models import ContactMsg
from django.utils.translation import gettext as _


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMsg
        fields = ['name', 'email', 'subject', 'msg']