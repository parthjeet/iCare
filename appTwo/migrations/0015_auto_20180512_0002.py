# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-12 00:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTwo', '0014_auto_20180511_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accmodel',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
