# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from classifieds.models import Post

# Register your models here.
admin.site.register(Post)
admin.site.site_header = "Zaneroo Admin Page"
