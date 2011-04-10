# -*- coding: utf-8 -*-
#
# Author:        alisue
# Date:            2010/12/27
#
from django.contrib import admin

from models import Material

class MaterialAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display    = ('__unicode__', 'is_public', 'is_downloadable', 'created_at', 'updated_at')
admin.site.register(Material, MaterialAdmin)
