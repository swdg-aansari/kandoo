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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
