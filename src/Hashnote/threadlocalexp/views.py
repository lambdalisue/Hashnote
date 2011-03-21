#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:    alisue
# Date:        2011/03/21
#
from django.http import HttpResponse
from django.template import Template, Context
from qwert.middleware import threadlocals

HTML = u"""
<!DOCTYPE html>
<html><head><meta charset=utf-8><title>threadlocals checker</title></head>
<body>
    <h1>threadlocals checker</h1>
    <p>あなたのスレッドIDは<strong>{{ thread_locals.id }}</strong>です。この番号をAlisueに教えてください。</p>
    {% if request != threadlocals_request %}
    <p><strong style="color: red;"><code>threadlocals</code>から取得した<code>request</code>と実際の<code>request</code>が
    異なります。下記情報も含めてAlisueにお知らせください</strong></p>
    
    <h2>Information</h2>
    <pre>
        _thread_locals: {{ thread_locals }}
        threadlocals.request: {{ threadlocals_request }}
        request = {{ request }}
    </pre>
    {% endif %}
</body></html>
"""
def check(request):
    _thread_locals = threadlocals._thread_locals
    _thread_locals.id = id(_thread_locals)
    t = Template(HTML)
    c = Context({
        'thread_locals': _thread_locals,
        'threadlocals_request': threadlocals.request(),
        'request': request,
    })
    response = HttpResponse(t.render(c))
    return response