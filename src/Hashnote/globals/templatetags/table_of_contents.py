# -*- coding: utf-8 -*-
#
# Author:        alisue
# Date:            2011/02/20
#
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

import re

register = template.Library()

@register.filter(name='toc')
@stringfilter
def table_of_contents(html, show_toc=None):

    LINK_CLASS = 'anchor'
    TOC_ID = 'toc'
    
    headlines = [x for x in re.finditer('<h(?P<type>\d)(?P<arguments>.*)>(?P<value>.*?)<\/h(?P=type)>', html)]
    if len(headlines) is 0:
        return html
    last_weight, toc = min([int(x.group('type')) for x in headlines]), ''
    for i, h in enumerate(headlines):
        type = h.group('type')
        arguments = h.group('arguments')
        value = h.group('value')
        current_weight = int(type)
        # Slug
        s = "hl%d" % i
        html = html.replace('<h%s%s>%s</h%s>' % (type, arguments, value, type),
                            '<h%s%s><a href="#%s" id="%s" class="%s">%s</a></h%s>' % (current_weight,
                                             arguments, s, s, LINK_CLASS, value, current_weight))
        if show_toc is not None:
            if (current_weight-last_weight) >= 1:
                toc = '%s\n\t<ul>\n' % toc[:-6] * (current_weight-last_weight)
            elif (last_weight-current_weight) >= 1:
                toc += '\t</ul>\n\t\t</li>\n'*(last_weight-current_weight)
            toc += '\t\t<li><a href="#%s">%s</a></li>\n' % (s, value)
            last_weight = current_weight
    if show_toc is not None:
        toc += '\t</ul>\n'*(toc.count('<ul>') - toc.count('</ul>'))
        toc += '\t\t</li>\n'*(toc.count('<li>') - toc.count('</li>'))
        toc = '<div id="%s">%s\n\t<ul>\n%s\t</ul>\n</div>' % (TOC_ID, show_toc, toc)
    return mark_safe('%s %s' % (toc, html))
