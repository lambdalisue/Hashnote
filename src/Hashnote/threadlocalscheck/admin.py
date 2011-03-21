#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:    alisue
# Date:        2011/03/21
#
from django.contrib import admin
from models import Threadlocals

class ThreadlocalsAdmin(admin.ModelAdmin):
    list_display    = ('threadlocals_id', 'ip_address', 'created_at')
    list_filter     = ('threadlocals_id', 'ip_address')
admin.site.register(Threadlocals, ThreadlocalsAdmin)