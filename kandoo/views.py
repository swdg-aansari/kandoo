__author__ = 'ali'
from django.shortcuts import render, redirect
from client.models import Client
from dastband.models import FriendshipBracelet
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import login
from User.forms import RegForm


def home(request):
    bracelets = FriendshipBracelet.objects.all()
    auth_form = AuthenticationForm(request)

    if request.method == 'POST':
        if request.user.is_authenticated():
            us = request.user
            client = Client.objects.get(user=us)
            selected_bracelets = request.POST.getlist('test')
            for obj in selected_bracelets:
                brc = FriendshipBracelet.objects.get(name=obj)
                client.bracelets.add(brc)
        else:
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                login(request, form.get_user())

    return render(request, 'home.html', {'form': auth_form})


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'create_account.html'
    success_url = reverse_lazy('home')


def user_creation(request):
    if request.method == 'POST':
        reg_form = RegForm(data=request.POST)
        if reg_form.is_valid():
            user = reg_form.save()
            Client.objects.create(user=user, name=reg_form.cleaned_data['name'])
            return redirect('home')
    else:
        reg_form = RegForm()
    return render(request, 'create_account.html', {'form': reg_form})
