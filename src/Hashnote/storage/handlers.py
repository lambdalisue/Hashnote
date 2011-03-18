#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:    alisue
# Date:        2011/03/01
#
from django.contrib.auth.decorators import permission_required
from piston.handler import BaseHandler
from piston.utils import rc, throttle, validate

from models import Material
from forms import MaterialForm

class MaterialHandler(BaseHandler):
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')
    fields = (
        'pk', 'is_public', 'is_downloadable',
        'title', 'description', 'file', 'created_at', 'updated_at'
    )
    model = Material

    def read(self, request, object_id=None):
        qs = Material.objects.published(request.user)
        
        if object_id:
            obj = qs.get(pk=object_id)
            return obj
        else:
            return qs

    @permission_required('storage.add_material')
    @throttle(5, 1*60)
    @validate(MaterialForm, 'POST')
    def create(self, request):
        instance = request.form.save()
        return instance
        
    @permission_required('storage.change_material')
    @throttle(5, 1*60)
    @validate(MaterialForm, 'PUT')
    def update(self, request, object_id):
        instance = request.form.save()
        return instance

    @permission_required('storage.delete_material')
    @throttle(5, 1*60)
    def delete(self, request, object_id):
        obj = Material.objects.get(pk=object_id)
        obj.delete()
        return rc.DELETED
