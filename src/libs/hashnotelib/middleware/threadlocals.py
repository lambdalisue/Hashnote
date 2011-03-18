# -*- coding: utf-8 -*-
#
# Author:        alisue
# Date:            2011/02/23
#
try:
    from threading import local
except ImportError:
    from django.utils._threading_local import local

__all__ = ['get_current_user', 'ThreadLocalsMiddleware']
_thread_locals = local()
def get_current_user():
    return getattr(_thread_locals, 'user', None)

class ThreadLocalsMiddleware(object):
    """Middleware that gets various objects from the request object and saves them in thread local storage."""
    def process_request(self, request):
        _thread_locals.user = getattr(request, 'user', None)