from django.db import models
from django.contrib.auth.models import User
from dastband.models import FriendshipBracelet


class Client(models.Model):
    name = models.CharField(max_length=20)
    user = models.OneToOneField(User)
    bracelets = models.ManyToManyField(FriendshipBracelet, blank=True)