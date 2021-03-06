# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-15 21:33
from __future__ import unicode_literals

from django.db import migrations, models
import music.models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_album_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.FileField(blank=True, null=True, upload_to=music.models.Album.upload_to),
        ),
        migrations.AlterField(
            model_name='artist',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
