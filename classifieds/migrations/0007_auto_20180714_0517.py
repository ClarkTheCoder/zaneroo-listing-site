# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-14 05:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifieds', '0006_auto_20180714_0515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now, null=True),
        ),
    ]