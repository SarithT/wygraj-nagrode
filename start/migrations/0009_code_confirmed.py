# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-24 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0008_auto_20170624_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
