# -*- coding: utf-8 -*-
#
# Author:        alisue
# Date:            2011/01/01
#
COMPRESS_CSS = {
    'default': {
        'source_filenames': (
            r'css/components/html5reset.css',
            #r'css/components/grid.css',
            r'css/components/typography.css',
            r'css/components/hlist.css',
            r'css/components/markdown.css',
            r'css/components/codehilite.css',
            r'css/components/pagination.css',
            r'css/components/controller.css',
            r'css/components/fenced.css',
            r'css/colors.css',
            r'css/components.css',
            r'css/layout.css',
        ),
        'output_filename': r'css/compressed/default.css',
        'extra_context': {
            'media': 'screen, projection',
        },
    },
    'blogs-article-detail': {
        'source_filenames': (
            r'css/layout/comment.css',
            r'css/layout/blogs-article-detail.css',
        ),
        'output_filename': r'css/compressed/blogs-article-detail.css',
        'extra_context': {
            'media': 'screen, projection',
        },
    },
    'blogs-article-list': {
        'source_filenames': (
            r'css/layout/blogs-article-list.css',
        ),
        'output_filename': r'css/compressed/blogs-article-list.css',
        'extra_context': {
            'media': 'screen, projection',
        },
    },
    'blogs-article-form': {
        'source_filenames': (
            r'css/layout/blogs-article-form.css',
        ),
        'output_filename': r'css/compressed/blogs-article-form.css',
        'extra_context': {
            'media': 'screen, projection',
        },
    },
    'storage-material-form': {
        'source_filenames': (
            r'css/layout/storage-material-form.css',
        ),
        'output_filename': r'css/compressed/storage-material-form.css',
        'extra_context': {
            'media': 'screen, projection',
        },
    },
    'storage-material-list': {
        'source_filenames': (
            r'css/layout/storage-material-form.css',
            r'css/layout/storage-material-list.css',
        ),
        'output_filename': r'css/compressed/storage-material-list.css',
        'extra_context': {
            'media': 'screen, projection',
        },
    },
    'storage-material-detail': {
        'source_filenames': (
            r'css/layout/storage-material-detail.css',
        ),
        'output_filename': r'css/compressed/storage-material-detail.css',
        'extra_context': {
            'media': 'screen, projection',
        },
    }, 
    'comments': {
        'source_filenames': (
            r'css/layout/comment.css',
        ),
        'output_filename': r'css/compressed/comments.css',
        'extra_context': {
            'media': 'screen, projection',
        },
    },
}
COMPRESS_JS = {
    'default': {
        'source_filenames': (
            r'javascript/plugins/jquery-1.4.4.min.js',
            r'javascript/plugins/jquery.footer-1.0.2.min.js',
            r'javascript/plugins/jquery.socialbutton-1.7.1.js',
            #r'javascript/plugins/jquery.updnWatermark.js',
            r'javascript/components/default.js',
        ),
        'output_filename': r'javascript/compressed/default.js',
    },
    'blogs-article-form': {
        'source_filenames': (
            r'javascript/components/blogs-article-form.js',
        ),
        'output_filename': r'javascript/compressed/blogs-article-form.js',
    },
}