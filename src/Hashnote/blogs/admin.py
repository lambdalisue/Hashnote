# -*- coding: utf-8 -*-
#
# Author:        alisue
# Date:            2010/12/27
#
from django.contrib import admin

from forms import ArticleForm
from models import Category, Article

class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm
    date_hierarchy = 'created_at'
    list_display    = ('__unicode__', 'created_at', 'updated_at', 'publish_at', 'is_draft')
    fieldsets = (
        (None, {
            'fields': ('title', ('category', 'is_draft'), 'body', 'tags'),
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('stylesheet', 'javascript', 'enable_comments')
        })
    )
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)