from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^utils/login/$',      'django.contrib.auth.views.login',      name='login'),
    url(r'^utils/logout/$',     'django.contrib.auth.views.logout',     name='logout'),
    url(r'^utils/admin/doc/',   include('django.contrib.admindocs.urls')),
    url(r'^utils/admin/',       include(admin.site.urls)),
    url(r'^comments/',          include('django.contrib.comments.urls')),
    url(r'^storage/',           include('Hashnote.storage.urls')),
    url(r'^',                   include('Hashnote.blogs.urls')),
    url(r'^threadlocalcheck/$', 'Hashnote.threadlocalexp.views.check')
)

from django.conf import settings
if settings.DEBUG:
    import os.path
    STATICS_PATH = os.path.join(os.path.dirname(__file__), '../../statics')
    document_root = lambda x: os.path.join(STATICS_PATH, x)
    urlpatterns += patterns('django.views.static',
        url(r'^css/(?P<path>.*)$',          'serve',    kwargs={'document_root': document_root('css')}),
        url(r'^javascript/(?P<path>.*)$',   'serve',    kwargs={'document_root': document_root('javascript')}),
        url(r'^image/(?P<path>.*)$',        'serve',    kwargs={'document_root': document_root('image')}),
    )