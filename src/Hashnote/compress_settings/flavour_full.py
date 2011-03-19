#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:    alisue
# Date:        2011/03/19
#
u"""CSS, JavaScript compressed settings for Desktop browser"""

COMPRESS_CSS = {
    'full-default': {
        'source_filenames': (
            r'css/full/components/typography.css',
            r'css/full/components/markdown.css',
            r'css/full/components/pagination.css',
            r'css/full/components/controller.css',
            r'css/full/components.css',
            r'css/full/layout.css',
        ),
        'output_filename': r'css/compressed/full-default.css',
        'extra_context': {
            'media': 'screen, projection',
        },
    },
    'full-blogs-article-detail': {
        'source_filenames': (
            r'css/full/views/comment.css',
            r'css/full/views/blogs-article-detail.css',
        ),
        'output_filename': r'css/compressed/full-blogs-article-detail.css',
        'extra_context': {
            'media': 'screen, projection',
        },
    },
    'full-blogs-article-list': {
        'source_filenames': (
            r'css/full/views/blogs-article-list.css',
        ),
        'output_filename': r'css/compressed/full-blogs-article-list.css',
        'extra_context': {
            'media': 'screen, projection',
        },
    },
    'full-blogs-article-form': {
        'source_filenames': (
            r'css/full/views/blogs-article-form.css',
        ),
        'output_filename': r'css/compressed/full-blogs-article-form.css',
        'extra_context': {
            'media': 'screen, projection',
        },
    },
    'full-storage-material-form': {
        'source_filenames': (
            r'css/full/views/storage-material-form.css',
        ),
        'output_filename': r'css/compressed/full-storage-material-form.css',
        'extra_context': {
            'media': 'screen, projection',
        },
    },
    'full-storage-material-list': {
        'source_filenames': (
            r'css/full/views/storage-material-form.css',
            r'css/full/views/storage-material-list.css',
        ),
        'output_filename': r'css/compressed/full-storage-material-list.css',
        'extra_context': {
            'media': 'screen, projection',
        },
    },
    'full-storage-material-detail': {
        'source_filenames': (
            r'css/full/views/storage-material-detail.css',
        ),
        'output_filename': r'css/compressed/full-storage-material-detail.css',
        'extra_context': {
            'media': 'screen, projection',
        },
    }, 
    'full-comments': {
        'source_filenames': (
            r'css/full/views/comment.css',
        ),
        'output_filename': r'css/compressed/full-comments.css',
        'extra_context': {
            'media': 'screen, projection',
        },
    },
}
COMPRESS_JS = {
    'full-default': {
        'source_filenames': (
            r'javascript/full/plugins/jquery.lightbox_me.js',
        ),
        'output_filename': r'javascript/compressed/full-default.js',
    },
    'full-blogs-article-form': {
        'source_filenames': (
            r'javascript/full/views/blogs-article-form.js',
        ),
        'output_filename': r'javascript/compressed/full-blogs-article-form.js',
    },
}