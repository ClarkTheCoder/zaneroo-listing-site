# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-17 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20180715_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='reputation',
            field=models.IntegerField(default=1),
        ),
    ]
