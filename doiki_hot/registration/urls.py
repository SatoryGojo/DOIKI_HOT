
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from .views import *

urlpatterns = [
    path('login/', authorization_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
]
