# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=150)
    price = models.CharField(max_length=100)
    body = models.TextField()
    contact_email = models.CharField(max_length=80, null=True)
    contact_number = models.IntegerField(default=250, null=True, blank=True)
    pub_date = models.DateTimeField(null=True, default=datetime.now)
    author = models.ForeignKey(User, null=True)
    category = models.CharField(max_length=150, null=True)
    picture = models.ImageField(upload_to='ad_pictures', default='', blank=True)



    def __str__(self):
        return self.title

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %d')

    def pub_date_pretty_extra(self):
        return self.pub_date.strftime('%b %d %Y')
