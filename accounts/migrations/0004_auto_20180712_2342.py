# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-12 23:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180712_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='', upload_to='profile_pics'),
        ),
    ]
