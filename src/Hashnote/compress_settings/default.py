# -*- coding: utf-8 -*-
#
# Author:        alisue
# Date:            2011/01/01
#
u"""CSS, JavaScript compressed settings for general use"""

COMPRESS_CSS = {
    'default': {
        'source_filenames': (
            r'css/components/html5reset.css',
            r'css/components/hlist.css',
            r'css/components/codehilite.css',
        ),
        'output_filename': r'css/compressed/default.css',
        'extra_context': {
            'media': 'screen, projection',
        },
    },
}
COMPRESS_JS = {
    'default': {
        'source_filenames': (
            r'javascript/plugins/jquery-1.4.4.min.js',
        ),
        'output_filename': r'javascript/compressed/default.js',
    },
}