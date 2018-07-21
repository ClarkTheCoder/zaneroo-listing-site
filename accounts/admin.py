# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from accounts.models import UserProfile

# Register your models here. IE Make them show up in admin panel :)

admin.site.register(UserProfile)
