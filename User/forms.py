__author__ = 'ali'
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegForm(UserCreationForm):
    name = forms.CharField(required=True, max_length=30)

    class Meta:
        model = User
        fields = ['username', 'name', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.name = self.cleaned_data['name']
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
