from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView

from .forms import *



def logout_user(request):
    logout(request)
    return redirect('home')


def authorization_user(request):
    if request.method == "POST":
        form = Authorization(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user and user.is_active:
                login(user=user, request=request)
                return redirect('home')
    else:
        form = Authorization()
        return render(request, 'registration/authorization.html', {'form': form})



def register(request):
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('home')

    else:
        form = Registration()
        return render(request, 'registration/registration.html', {'form': form})







