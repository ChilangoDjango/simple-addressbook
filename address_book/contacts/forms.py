from django import forms
from . import models

class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        exclude = ['user',]

class GroupForm(forms.ModelForm):
    class Meta:
        model = models.Group
        exclude = ['user',]
