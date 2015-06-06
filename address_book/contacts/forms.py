from django import forms
from . import models

class ContactForm(forms.ModelForm):

    def save(self, usuario=None):
        self.instance.user = usuario
        super(ContactForm, self).save()

    class Meta:
        model = models.Contact
        exclude = ['user',]

class GroupForm(forms.ModelForm):

    def save(self, usuario=None):
        self.instance.user = usuario
        super(GroupForm, self).save()

    class Meta:
        model = models.Group
        exclude = ['user',]
