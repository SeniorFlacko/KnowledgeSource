# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recursos', '0001_initial'),
        ('playlists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='playlist_recurso',
            field=models.ManyToManyField(to='recursos.Recurso'),
        ),
    ]