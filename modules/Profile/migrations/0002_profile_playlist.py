# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 14:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('playlists', '0001_initial'),
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='playlist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playlists.Playlist'),
        ),
    ]