# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-04 01:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0011_songupdatetoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='download_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
