from django.db import models


# Create your models here.
class FriendshipBracelet(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    picture = models.ImageField(upload_to='', default='static/picture.jpg')



