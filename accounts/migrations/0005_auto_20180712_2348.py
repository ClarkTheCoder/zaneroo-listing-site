# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-12 23:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180712_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='media/profile_pics/default.jpg', upload_to='profile_pics'),
        ),
    ]