# -*- coding: utf-8 -*-
#
# Author:        alisue
# Date:            2011/01/03
#
from django.db import models
from django.utils.text import ugettext_lazy as _

from tagging.fields import TagField
from tagging.models import Tag

from hashnotelib.middleware.threadlocals import get_current_user

from datetime import date

class ArticleManager(models.Manager):
    u"""Manager of Article Model"""
    def published(self):
        u"""Return non draft article queryset"""
        return self.filter(is_draft=False)
    
    def draft(self):
        u"""Return draft article queryset"""
        return self.filter(is_draft=True)
    
class Category(models.Model):
    u"""Blog category model"""
    label   = models.CharField(_('label'), max_length=100, unique=True)
    
    class Meta:
        ordering            = ('label',)
        verbose_name        = _('category')
        verbose_name_plural = _('categories')
        
    def __unicode__(self):
        return self.label
    
    @models.permalink
    def get_absolute_url(self):
        return ('blogs_category_detail', (), {'object_id': self.pk})
    
class Article(models.Model):
    u"""Blog article model"""
    is_draft        = models.BooleanField(_('is draft'), default=False, help_text=_('Check this for saving article as draft.'))
    title           = models.CharField(_('title'), max_length=100, default=_('No title'))
    body            = models.TextField(_('body'))
    category        = models.ForeignKey(Category, verbose_name=_('category'), related_name='articles', blank=True, null=True)
    tags            = TagField(_('tags'))
    # Optionally
    stylesheet      = models.TextField(_('stylesheet'), blank=True, help_text=_('Optional stylesheet for this article'))
    javascript      = models.TextField(_('javascript'), blank=True, help_text=_('Optional javascript for this article'))
    enable_comments = models.BooleanField(_('enable comments'), default=True)
    # Automatically
    publish_at      = models.DateField(_('date published'), null=True, editable=False)
    created_at      = models.DateTimeField(_('date time created'), auto_now=True)
    updated_at      = models.DateTimeField(_('date time updated'), auto_now_add=True)
    
    objects         = ArticleManager()
    
    class Meta:
        get_latest_by       = ('updated_at',)
        ordering            = ('title',)
        unique_together     = ('title', 'publish_at')
        verbose_name        = _('article')
        verbose_name_plural = _('articles')
        
    def __unicode__(self):
        return self.title
    
    @models.permalink
    def get_absolute_url(self):
        if self.is_draft:
            return ('blogs_article_update', (), {'object_id': self.pk})
        else:
            return ('blogs_article_detail', (), {
                'year': self.publish_at.year,
                'month': self.publish_at.month,
                'day': self.publish_at.day,
                'object_id': self.pk,
            })
    
    def clean(self, **kwargs):
        if self.is_draft and self.publish_at:
            self.publish_at = None
        elif not self.is_draft and not self.publish_at:
            self.publish_at = date.today()
        super(Article, self).clean(**kwargs)
        
    def validate_unique(self, exclude=None):
        if isinstance(exclude, (list, tuple)):
            if 'publish_at' in exclude: exclude.remove('publish_at')
        super(Article, self).validate_unique(exclude)
    
from django.contrib.comments.moderation import CommentModerator, moderator, AlreadyModerated
class ArticleModerator(CommentModerator):
    email_notification = True
    enable_field = 'enable_comments'
try:
    moderator.register(Article, ArticleModerator)
except AlreadyModerated:
    pass
