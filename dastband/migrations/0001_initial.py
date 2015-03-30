# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FriendshipBracelet',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('picture', models.ImageField(default='static/picture.jpg', upload_to='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
