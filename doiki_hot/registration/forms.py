from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class Authorization(forms.Form):
    username = forms.CharField(widget=forms.TextInput(), label = 'Логин')
    password = forms.CharField(widget=forms.PasswordInput(), label='Пароль')



class Registration(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(), label='Логин')
    password = forms.CharField(widget=forms.PasswordInput(), label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Повтор пароля')
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password', 'password2')

