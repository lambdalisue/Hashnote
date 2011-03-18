# -*- coding: utf-8 -*-
#
# Author:        alisue
# Date:            2011/02/21
#
from django.conf import settings
from django.http import HttpResponse

import watermark

try:
    from PIL import Image
except ImportError:
    import Image

def image_response(image, size=None):
    u"""Render image to HttpResponse and return it
    
    If `size` is specified, rendered image will be thumbnail to the size.
    
    Attributes:
        image       - PIL.Image instance
        size        - thumbnail size represented by list like (w, h) (Default: None)
    
    Return:
        response    - HttpResponse instance
    """
    if size:
        image.thumbnail(size, Image.ANTIALIAS)
    response = HttpResponse(mimetype='image/png')
    image.save(response, 'PNG')
    return response

def watermark_response(image, type='tile', wm=None, size=None):
    u"""Render image with watermark to HttpResponse and return it
    
    If `size` is specified, rendered image will be thumbnail to the size.
    If `watermark` is specified, that is used insted of PIL.Image created 
    by `settings.STORAGE_WATERMARK_PATH`.
    
    Attribute:
        image        - PIL.Image instance
        type         - Watermark rendering type
        wm           - PIL.Image instance for watermark (Default: None)
        size         - thumbnail size represented by list like (w, h) (Default: None)
    
    Return:
        response     - HttpResponse instance
    """
    if size:
        image.thumbnail(size, Image.ANTIALIAS)
    
    if not wm:
        WATERMARK = settings.STORAGE_WATERMARK_PATH
        wm = Image.open(WATERMARK)
    elif not isinstance(wm, Image):
        raise AttributeError('`watermark` attribute must be PIL.Image instance')
    image = watermark.watermark(image, wm, 'tile', 0.3)
    response = HttpResponse(mimetype='image/png')
    image.save(response, 'PNG')
    return response