# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-18 21:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTwo', '0016_gpsmodel_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='accmodel',
            name='isPressed',
            field=models.CharField(default='NULL', max_length=128),
        ),
    ]