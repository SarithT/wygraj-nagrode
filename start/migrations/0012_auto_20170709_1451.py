# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-09 14:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0011_auto_20170709_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='prize',
            field=models.CharField(choices=[('Samsung Galaxy S8', 'Samsung Galaxy S8'), ('IPhone 7', 'IPhone 7')], default='SGS8', max_length=20),
        ),
    ]
