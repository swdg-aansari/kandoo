__author__ = 'ali'
from django.shortcuts import render
from dastband.models import FriendshipBracelet


def home(request):
    #bracelets = FriendshipBracelet.objects.get(name = ObjectName)
    return render(request,'home.html')
