from django.db import models


# Create your models here.
class FriendshipBracelet(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    price = models.IntegerField()
   # picture = models.ImageField(upload_to="pics")



