from django import forms
from django.forms import fields
from blog.models import ContactModel


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ('email', 'fullname', 'message')
