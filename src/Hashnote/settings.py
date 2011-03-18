# -*- coding: utf-8 -*-
#
# Author:        alisue
# Date:            2011/01/01
#
#------------------------------------------------------------------------------------------
import sys
import os.path
ROOT = os.path.join(os.path.dirname(__file__), '../../')
PYTHON_PATHS = [
    os.path.join(ROOT, 'src/libs'),
]
sys.path += PYTHON_PATHS
#------------------------------------------------------------------------------------------

VERSION = '0.0.0.1'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

INTERNAL_IPS = (
    '127.0.0.1',
)

ADMINS = (
)

MANAGERS = ADMINS
      
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',     # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(ROOT, 'hashnote.db'),  # Or path to database file if using sqlite3.
        'USER': '',                                 # Not used with sqlite3.
        'PASSWORD': '',                             # Not used with sqlite3.
        'HOST': '',                                 # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                                 # Set to empty string for default. Not used with sqlite3.
    },
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
#TIME_ZONE = 'America/Chicago'
TIME_ZONE = 'Tokyo/Japan'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ja_JP'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(ROOT, 'statics')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '(e$5ibv8f=8#-%j_a4^snt3^eeh@05k^@&(0&1dc192ai3yq-4'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
)

MIDDLEWARE_CLASSES = (
    #'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'hashnotelib.middleware.http.Http403Middleware',
    'hashnotelib.middleware.threadlocals.ThreadLocalsMiddleware',
    'hashnotelib.middleware.exception.UserBasedExceptionMiddleware',
    #'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'Hashnote.urls'

TEMPLATE_DIRS = (
    os.path.join(ROOT, 'templates/default'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.comments',
    # site-package
    'compress',
    'pagination',
    'reversetag',
    'codemirror',
    'markitup',
    'tagging',
    'modify_history',
    'Hashnote.globals',
    'Hashnote.blogs',
    'Hashnote.storage',
)

FIXTURE_DIRS = (
    os.path.join(ROOT, 'fixtures'),
)

# django-compress
#------------------------------------------------------
import compress_settings
COMPRESS_CSS = compress_settings.COMPRESS_CSS
COMPRESS_JS = compress_settings.COMPRESS_JS


# django.contrib.auth
#----------------------------------------------------------------------------
LOGIN_REDIRECT_URL  = "/"
LOGIN_URL = "/registration/login/"
LOGOUT_URL = "/registration/logout/"

EMAIL_HOST = 'localhost'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 25
EMAIL_USE_TLS = True
DEFAULT_EMAIL = 'webmaster@hashnote.net'
DEFAULT_FROM_EMAIL = DEFAULT_EMAIL

# MarkItUpTextarea
#------------------------------------------------------------------------------
MARKITUP_PATH = r'javascript/markitup'
MARKITUP_DEFAULT_SET = 'markdown'
MARKITUP_DEFAULT_SKIN = 'simple'

# CodeMirrorTextarea
#------------------------------------------------------------------------------
CODEMIRROR_PATH = r'javascript/codemirror/js'

# Akismet
#------------------------------------------------------------------------------
AKISMET_API_KEY = r'your akismet api key'

try:
    from local_settings import *
except ImportError:
    pass
