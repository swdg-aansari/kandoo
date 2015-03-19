__author__ = 'ali'
from django.shortcuts import render
from django.shortcuts import render_to_response

from dastband.models import FriendshipBracelet


def home(request):
    bracelets = FriendshipBracelet.objects.get(name='sade')
    return render_to_response('home.html', {'bracelets_objects': bracelets})

