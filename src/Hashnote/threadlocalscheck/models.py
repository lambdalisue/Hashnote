#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:    alisue
# Date:        2011/03/21
#
from django.db import models
from django.contrib import admin

class Threadlocals(models.Model):
    threadlocals_id = models.CharField('threadlocals id', max_length=255)
    ip_address      = models.IPAddressField('ip address')
    created_at      = models.DateTimeField('date created', auto_now_add=True)
    
class ThreadlocalsAdmin(admin.ModelAdmin):
    list_display    = ('threadlocals_id', 'ip_address', 'created_at')
    list_filter     = ('threadlocals_id', 'ip_address')
admin.site.register(Threadlocals, ThreadlocalsAdmin)