from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    type_number = models.CharField(max_length=255)
    number = models.IntegerField()
    user = models.ForeignKey(User)


class Group(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    user = models.ForeignKey(User)
    contact = models.ManyToManyField(Contact)
