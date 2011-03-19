#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:    alisue
# Date:        2011/03/19
#
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from qwert.templatetags.markdown_tags import markdown
from Hashnote.storage.templatetags.storage_tags import parse_storage

register = template.Library()

@register.filter
@stringfilter
def parseall(value):
    value = markdown(value, arg="extra,codehilite(force_linenos=True)")
    value = parse_storage(value)
    return mark_safe(value)
