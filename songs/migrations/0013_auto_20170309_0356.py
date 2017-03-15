# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 03:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0012_song_download_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='songupdatetoken',
            name='last_finished',
        ),
        migrations.RemoveField(
            model_name='songupdatetoken',
            name='last_started',
        ),
        migrations.AddField(
            model_name='songupdatetoken',
            name='finished',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='songupdatetoken',
            name='started',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]