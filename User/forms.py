__author__ = 'ali'
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegForm(UserCreationForm):
    name = forms.CharField(required=True, max_length=30)

    class Meta:
        model = User
        fields = ['username', 'name', 'password1', 'password2']
