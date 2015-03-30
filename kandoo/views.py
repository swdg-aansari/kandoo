__author__ = 'ali'
from django.shortcuts import render_to_response
from django.template import RequestContext
from client.models import Client

from dastband.models import FriendshipBracelet


def home(request):
    bracelets = FriendshipBracelet.objects.all()
    client = Client.objects.get(name='sade')
    print(client.name)
    if request.method == 'POST':
        selected_bracelets = request.POST.getlist('test')

        # for obj in selected_bracelets:
        #     client.bracelets.add(obj)

    return render_to_response('home.html', context_instance=RequestContext(request))


