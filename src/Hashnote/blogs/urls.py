# -*- coding: utf-8 -*-
#
# Author:        alisue
# Date:            2011/02/27
#
from django.conf.urls.defaults import *

import views

update_patterns = patterns('',
    url(r'^create/$',                       views.create_article,           name='blogs_article_create'),
    url(r'^update/(?P<object_id>\d+)/$',    views.update_article,           name='blogs_article_update'),
    url(r'^delete/(?P<object_id>\d+)/$',    views.delete_article,           name='blogs_article_delete'),
)
view_patterns = patterns('',
    url(r'^$',                              views.article_archive_index,    name='blogs_article_list'),
    url(r'^tags/(?P<tag>[^/]+)/$',          views.tagged_article_list,      name='blogs_article_tagged_list'),
    url(r'^today/$',                        views.article_archive_today,    name='blogs_article_archive_today'),
    url(r'^(?P<year>\d{4})/$',              views.article_archive_year,     name='blogs_article_archive_year'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$',
        views.article_archive_month,        name='blogs_article_archive_month'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$',
        views.article_archive_day,          name='blogs_article_archive_day'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<object_id>\d+)/$',
        views.article_detail,               name='blogs_article_detail'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<object_id>\d+)\.raw$',
        views.article_detail_raw,           name='blogs_article_detail_raw'),
)
urlpatterns = patterns('',
    url(r'^',                           include(update_patterns)),
    url(r'^',                           include(view_patterns)),
)