# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 07:36
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0005_auto_20170301_0721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
        migrations.AlterField(
            model_name='song',
            name='url',
            field=models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
        migrations.AlterField(
            model_name='tag',
            name='text',
            field=models.CharField(max_length=255, unique=True, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
    ]