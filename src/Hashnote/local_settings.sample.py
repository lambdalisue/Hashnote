# -*- coding: utf-8 -*-
#
# Override settings with local_settings.py
# Used for deploy or whatever
#
DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'mysql',                          # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                                 # Or path to database file if using sqlite3.
        'USER': '',                                 # Not used with sqlite3.
        'PASSWORD': '',                             # Not used with sqlite3.
        'HOST': '',                                 # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                                 # Set to empty string for default. Not used with sqlite3.
    },
}

# Make this unique, and don't share it with anybody.
#------------------------------------------------------------------------------
SECRET_KEY = 'the secret key'

# Cache backend
#------------------------------------------------------------------------------
CACHE_BACKEND = 'memcached://127.0.0.1:11211'

# Akismet
#------------------------------------------------------------------------------
AKISMET_API_KEY = r'your akismet api key'
