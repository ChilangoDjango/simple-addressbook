from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse

def home(request):
    return redirect(reverse('contacts:login'))

def login(request):
    template_response = 'contacts/login.html'
    if request.method=='POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                #Dirigir a pantalla principal
            else:
                messages.error(request, u'Usuario/Password incorrecto')
                return render(request, template_response, {'form': form})
        else:
            return render(request, template_response, {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, template_response, {'form': form})

def singup(request):
    template_response = 'contacts/singup.html'
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('contacts:login'))
        else:
            return render(request, template_response, {'form': form})
    else:
        form = UserCreationForm()
        return render(request, template_response, {'form': form})
