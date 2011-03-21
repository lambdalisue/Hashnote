#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:    alisue
# Date:        2011/03/21
#
from django.http import HttpResponse
from django.template import Template, Context
from qwert.middleware import threadlocals

from models import Threadlocals

HTML = u"""
<!DOCTYPE html>
<html><head><meta charset=utf-8><title>threadlocals checker</title></head>
<body>
    <h1>threadlocals checker</h1>
    <p>あなたのスレッドIDは<strong>{{ thread_locals.id }}</strong>です。この番号をAlisueに教えてください。</p>
    
    <p>あなたのIP Addressで{{ exists.count }}個のスレッドIDが保存されています</p>
    
    {% if conflicts.count > 0 %}
    <p><strong style="color: red;">{{ conflicts.count }}個の衝突が見つかりました！下記情報も含めてAlisueにお知らせください</strong></p>
    <ul>
        {% for conflict in conflicts %}
        <li>{{ conflict.threadlocals_id }}</li>
        {% endfor %}
    </ul>
    {% endif %}
    
    {% if request != threadlocals_request %}
    <p><strong style="color: red;"><code>threadlocals</code>から取得した<code>request</code>と実際の<code>request</code>が
    異なります。下記情報も含めてAlisueにお知らせください</strong></p>
    
    <pre>
        _thread_locals: {{ thread_locals }}
        threadlocals.request: {{ threadlocals_request }}
        request = {{ request }}
    </pre>
    {% endif %}
</body></html>
"""
def check(request):
    threadlocals_id = id(threadlocals._thread_locals)
    ip_address = request.META['REMOTE_ADDR']
    # Save
    Threadlocals(
        threadlocals_id = threadlocals_id,
        ip_address=ip_address,
    ).save()
    
    exists = Threadlocals.objects.filter(ip_address=ip_address)
    conflicts = Threadlocals.objects.exclude(ip_address=ip_address).filter(threadlocals_id=threadlocals_id)
    
    t = Template(HTML)
    c = Context({
        'threadlocals_id': threadlocals_id,
        'exists': exists,
        'conflicts': conflicts,
        'thread_locals': threadlocals._thread_locals,
        'threadlocals_request': threadlocals.request(),
        'request': request,
    })
    response = HttpResponse(t.render(c))
    return response