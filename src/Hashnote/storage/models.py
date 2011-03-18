# -*- coding: utf-8 -*-
#
# Author:        alisue
# Date:            2011/02/21
#
from django.db import models
from django.utils.text import ugettext_lazy as _

import utils.html as html
import utils.filetypes as filetypes
import mimetypes
import os.path

class MaterialManager(models.Manager):
    u"""Storage material manager"""
    def published(self, user):
        u"""Return public material queryset"""
        if user.is_authenticated():
            return self.all()
        else:
            return self.filter(is_public=True)
        
class Material(models.Model):
    u"""Storage material model"""
    def _get_upload_path(self, filename):
        path = r'storage'
        return os.path.join(path, filename)
    file            = models.FileField(_('file'), upload_to=_get_upload_path)
    # Optional
    title           = models.CharField(_('title'), max_length=255, blank=True)
    description     = models.TextField(_('description'), blank=True)
    is_public       = models.BooleanField(_('is public'), default=True, help_text=_('uncheck it for hide file for anonymous users'))
    is_downloadable = models.BooleanField(_('is downloadable'), default=True, help_text=_('uncheck it for disable download for anonymous users'))
    # Uneditable
    created_at      = models.DateTimeField(_('date created'), auto_now_add=True)
    updated_at      = models.DateTimeField(_('date updated'), auto_now=True)
    
    objects         = MaterialManager()
    
    class Meta:
        ordering            = ('-updated_at', '-created_at', 'title')
        verbose_name        = _('material')
        verbose_name_plural = _('materials')
    
    def __unicode__(self):
        return self.title
    
    @models.permalink
    def get_absolute_url(self):
        return ('storage_material_detail', (), {'object_id': self.pk})
    @models.permalink
    def get_download_url(self):
        return ('storage_material_download', (), {'object_id': self.pk})
    @models.permalink
    def get_preview_url(self):
        return ('storage_material_preview', (), {'object_id': self.pk})
    @models.permalink
    def get_digest_url(self):
        return ('storage_material_digest', (), {'object_id': self.pk})
    @models.permalink
    def get_thumbnail_url(self):
        return ('storage_material_thumbnail', (), {'object_id': self.pk})
    
    @property
    def filename(self):
        path = self.file.name
        return os.path.basename(path)
    @property
    def mimetype(self):
        try:
            mimetypes.init()
            return mimetypes.guess_type(self.filename)[0]
        except:
            return None
    @property
    def filetype(self):
        return filetypes.guess(self.filename)
    
    def get_thumbnail_display(self):
        return html.thumbnail_html(self, 320, 240)
    def get_download_display(self):
        return html._download_link(self.get_download_url(), self.file, self.mimetype)
    
    def clean(self, request=None):
        if not self.title:
            self.title = self.file.name
        super(Material, self).clean()
