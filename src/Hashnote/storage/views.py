# -*- coding: utf-8 -*-
#
# Author:        alisue
# Date:            2011/02/21
#
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.views.generic import list_detail
from django.views.generic import create_update
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import permission_required

from hashnotelib.http import Http403
from models import Material
from forms import MaterialForm, MaterialDescriptionForm, MaterialDescriptionUpdateForm
import utils
import urllib
import os.path

try:
    from PIL import Image
except ImportError:
    import Image
    
#
# list_detail
#---------------------------------------------------------
def material_list(request):
    kwargs = {
        'queryset': Material.objects.published(request.user),
        'extra_context': {
            'form': MaterialForm(),
        }
    }
    return list_detail.object_list(request, **kwargs)

def material_detail(request, object_id):
    kwargs = {
        'queryset': Material.objects.published(request.user)
    }
    return list_detail.object_detail(request, object_id=object_id, **kwargs)

@never_cache
def material_download(request, object_id):
    qs = Material.objects.published(request.user)
    obj = get_object_or_404(qs, pk=object_id)
    if not request.user.is_authenticated() and not obj.is_downloadable:
        raise Http403
    # Create Response
    response = HttpResponse(obj.file)
    response['Cache-Control'] = 'no-cache'
    response['Content-Type'] = 'application/octet-stream'
    # Browser
    USER_AGENT = request.META['HTTP_USER_AGENT'].lower()
    if 'webkit' in USER_AGENT:
        # Safari/Chrome
        response['Content-Disposition'] = (u'attachement; filename=%s'%obj.filename).encode('utf-8')
    elif 'msie' in USER_AGENT:
        # Internet Explorer
        filename = urllib.quote(obj.filename.encode('utf-8'))
        response['Content-Disposition'] = u'attachement; filename=%s' % filename
    else:
        # Opera/Firefox/etc...
        filename = urllib.quote(obj.filename.encode('utf-8'))
        response['Content-Disposition'] = u'attachement; filename*=UTF-8\'\'%s' % filename
    return response

def material_preview(request, object_id):
    qs = Material.objects.all()
    obj = get_object_or_404(qs, pk=object_id)
    if not request.user.is_authenticated() and not obj.is_public:
        raise Http403
    if obj.filetype == 'image':
        w = settings.STORAGE_PREVIEW_WIDTH
        h = settings.STORAGE_PREVIEW_HEIGHT
        img = Image.open(obj.file)
        if settings.STORAGE_WATERMARK_PATH:
            return utils.watermark_response(img, Image.open(settings.STORAGE_WATERMARK_PATH), size=(w, h))
        else:
            return utils.image_response(img, size=(w, h))
    else:
        response = HttpResponse(obj.file, mimetype=obj.mimetype)
        return response
    
def material_thumbnail(request, object_id):
    obj = get_object_or_404(Material, pk=object_id)
    if not request.user.is_authenticated() and not obj.is_public:
        raise Http403
    mimetype = obj.mimetype
    filetype = obj.filetype
    width = int(request.GET.get('width', 320))
    height = int(request.GET.get('height', 240))
    if "image" == filetype:
        return utils.image_response(Image.open(obj.file), (width, height))
    else:
        response = HttpResponse(obj.file, mimetype=mimetype)
        return response
    
def material_digest(request, object_id):
    PATH = {
        'image': r'image/storage/Image.png',
        'audio': r'image/storage/Headphone.png',
        'archive': r'image/storage/Box.png',
        'text': r'image/storage/File.png',
        'application': r'image/storage/Software.png',
        'unknown': r'image/storage/Question 4.png',
    }
    SIZE = (172, 129)
    obj = get_object_or_404(Material, pk=object_id)
    if not request.user.is_authenticated() and not obj.is_public:
        raise Http403
    filetype = obj.filetype
    if filetype == 'image':
        img = Image.open(obj.file)
    else:
        filename = os.path.join(settings.MEDIA_ROOT, PATH[filetype])
        img = Image.open(filename)
    return utils.image_response(img, SIZE)

@permission_required('storage.add_material')
def create_material(request):
    kwargs = {
        'form_class': MaterialDescriptionForm,
    }
    if request.GET.get('next', None):
        kwargs['post_save_redirect'] = request.GET.get('next')
    return create_update.create_object(request, **kwargs)
   
@permission_required('storage.change_material')
def update_material(request, object_id):
    kwargs = {
        'form_class': MaterialDescriptionUpdateForm,
    }
    return create_update.update_object(request, object_id=object_id, **kwargs)
    
@permission_required('storage.delete_material')
def delete_material(request, object_id):
    kwargs = {
        'model': Material,
        'post_delete_redirect': reverse('storage_material_list'),
    }
    return create_update.delete_object(request, object_id=object_id, **kwargs)