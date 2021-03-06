# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 23:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='dislike_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='like_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='tags',
            field=models.ManyToManyField(null=True, to='songs.Tag'),
        ),
        migrations.AlterField(
            model_name='song',
            name='thumbnail_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='view_count',
            field=models.IntegerField(null=True),
        ),
    ]
