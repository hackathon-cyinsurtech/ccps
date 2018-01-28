# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin

from api.models import Profile, Metric

admin.site.register(Profile)
admin.site.register(Metric)
