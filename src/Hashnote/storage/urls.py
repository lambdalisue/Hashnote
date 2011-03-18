# -*- coding: utf-8 -*-
#
# Author:        alisue
# Date:            2011/02/27
#
from django.conf.urls.defaults import *

import views

update_patterns = patterns('',
    url(r'^create/$',                       views.create_material,          name='storage_material_create'),
    url(r'^update/(?P<object_id>\d+)/$',    views.update_material,          name='storage_material_update'),
    url(r'^delete/(?P<object_id>\d+)/$',    views.delete_material,          name='storage_material_delete'),
)
detail_patterns = patterns('',
    url(r'^$',                              views.material_detail,          name='storage_material_detail'),
    url(r'^preview/$',                      views.material_preview,         name='storage_material_preview'),
    url(r'^download/$',                     views.material_download,        name='storage_material_download'),
    url(r'^digest/$',                       views.material_digest,          name='storage_material_digest'),
    url(r'^thumbnail/$',                    views.material_thumbnail,       name='storage_material_thumbnail'),
)
view_patterns = patterns('',
    url(r'^$',                              views.material_list,            name='storage_material_list'),
    url(r'^(?P<object_id>\d+)/',            include(detail_patterns)),
)
urlpatterns = patterns('',
    url(r'^',                               include(update_patterns)),
    url(r'^',                               include(view_patterns)),
)