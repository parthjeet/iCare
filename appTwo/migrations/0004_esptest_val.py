# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-06 08:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTwo', '0003_esptest_sensr'),
    ]

    operations = [
        migrations.AddField(
            model_name='esptest',
            name='val',
            field=models.CharField(default='NULL', max_length=128),
        ),
    ]
