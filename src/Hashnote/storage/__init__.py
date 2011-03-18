# -*- coding: utf-8 -*-
#
# Author:        alisue
# Date:            2010/11/28
#
from django.conf import settings

settings.STORAGE_PREVIEW_WIDTH = getattr(settings, 'STORAGE_PREVIEW_WIDTH', 640)
settings.STORAGE_PREVIEW_HEIGHT = getattr(settings, 'STORAGE_PREVIEW_HEIGHT', 480)
settings.STORAGE_WATERMARK_PATH = getattr(settings, 'STORAGE_WATERMARK_PATH', None)