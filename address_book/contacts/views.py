from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from . import forms
from . import models


def home(request):
    return redirect(reverse('contacts:login'))

def login_user(request):
    template_response = 'contacts/login.html'
    if request.method=='POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect(reverse('contacts:show_contacts'))
        else:
            messages.error(request, u'Usuario/Password incorrecto')
            return render(request, template_response, {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, template_response, {'form': form})

def singup(request):
    template_response = 'contacts/singup.html'
    if request.method=='POST':
        print "dddddd"
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('contacts:login'))
        else:
            return render(request, template_response, {'form': form})
    else:
        form = UserCreationForm()
        return render(request, template_response, {'form': form})

def new_contact(request):
    template_response = 'contacts/new_contact.html'
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            form.save(usuario=request.user)
            return redirect(reverse('contacts:show_contacts'))
        else:
            return render(request, template_response, {'form': form})
    else:
        form = forms.ContactForm()
        return render(request, template_response, {'form': form})

def show_contacts(request):
    template_response = 'contacts/show_contacts.html'
    contacts = models.Contact.objects.filter(user=request.user)
    print contacts
    return render(request, template_response, {'contacts': contacts})


def edit_contact(request, id_contact):
    template_response = 'contacts/edit_contact.html'
    contact = models.Contact.objects.get(pk=id_contact, user=request.user)
    if request.method == 'POST':
        form = forms.ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save(usuario=request.user)
            return redirect(reverse('contacts:show_contacts'))
        else:
            return render(request, template_response, {'form': form})
    else:
        form = forms.ContactForm(instance=contact)
        return render(request, template_response, {'form': form})

def delete_contact(request, id_contact):
    contact = models.Contact.objects.get(pk=id_contact, user=request.user)
    contact.delete()
    return redirect(reverse('contacts:show_contacts'))
