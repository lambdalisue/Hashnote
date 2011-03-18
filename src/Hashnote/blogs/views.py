# -*- coding: utf-8 -*-
#
# Author:        alisue
# Date:            2011/01/02
#
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.views.generic import date_based
from django.views.generic import create_update
from django.contrib.auth.decorators import permission_required
from tagging.views import tagged_object_list

from models import Category, Article
from forms import ArticleForm, CategoryForm


# tagged_object_list
#----------------------------------------------------------------------
def tagged_article_list(request, tag):
    kwargs = {
        'queryset_or_model': Article.objects.published(),
        'allow_empty': True,
    }
    return tagged_object_list(request, tag=tag, **kwargs)

# list_detail
#----------------------------------------------------------------------
def article_archive_index(request, ):
    kwargs = {
        'queryset': Article.objects.published(),
        'date_field': 'publish_at',
        'template_object_name': 'object_list',
        'template_name': r'blogs/article_list.html',
    }
    return date_based.archive_index(request, **kwargs)
def article_archive_year(request, year):
    kwargs = {
        'queryset': Article.objects.published(),
        'date_field': 'publish_at',
    }
    return date_based.archive_year(request, year=year, **kwargs)
def article_archive_month(request, year, month):
    kwargs = {
        'queryset': Article.objects.published(),
        'date_field': 'publish_at',
        'month_format': '%m',
    }
    return date_based.archive_month(request, year=year, month=month, **kwargs)
def article_archive_day(request, year, month, day):
    kwargs = {
        'queryset': Article.objects.published(),
        'date_field': 'publish_at',
        'month_format': '%m',
    }
    return date_based.archive_day(request, year=year, month=month, day=day, **kwargs)
def article_archive_today(request):
    kwargs = {
        'queryset': Article.objects.published(),
        'date_field': 'publish_at',
    }
    return date_based.archive_today(request, **kwargs)
def article_detail(request, year, month, day, object_id):
    kwargs = {
        'queryset': Article.objects.published(),
        'date_field': 'publish_at',
        'month_format': '%m',
    }
    return date_based.object_detail(request, year=year, month=month, day=day, object_id=object_id, **kwargs)
def article_detail_raw(request, author, year, month, day, object_id):
    qs = Article.objects.published(author)
    kwargs = {
        'publish_at__year': year,
        'publish_at__month': month,
        'publish_at__day': day,
    }
    qs = qs.filter(**kwargs)
    obj = get_object_or_404(qs, pk=object_id)
    html = "<pre>%s</pre>" % obj.body
    return HttpResponse(html)
    
# create_update
#------------------------------------------------------------------------
@permission_required('blogs.add_article')
def create_article(request):
    kwargs = {
        'form_class': ArticleForm,
    }
    return create_update.create_object(request, **kwargs)
@permission_required('blogs.change_article')
def update_article(request, object_id):
    kwargs = {
        'form_class': ArticleForm,
    }
    return create_update.update_object(request, object_id=object_id, **kwargs)
@permission_required('blogs.delete_article')
def delete_article(request, object_id):
    kwargs = {
        'model': Article,
        'post_delete_redirect': reverse('blogs_article_list'),
    }
    return create_update.delete_object(request, **kwargs)