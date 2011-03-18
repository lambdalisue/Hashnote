# -*- coding: utf-8 -*-
#
# Author:        alisue
# Date:            2011/01/02
#
from django import forms
from models import Article, Category

from markitup.widgets import MarkItUpTextarea
from codemirror.widgets import CodeMirrorTextarea
CSS_CODEMIRROR_ATTRS = {
    'parserfile': r'parsecss.js',
    'stylesheet': r'javascript/codemirror/css/csscolors.css',
}
JS_CODEMIRROR_ATTRS = {
    'parserfile': [r'parsejavascript.js', r'tokenizejavascript.js'],
    'stylesheet': r'javascript/codemirror/css/jscolors.css',
}

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = (
            'title', 'category', 'is_draft', 'tags', 'body', 'stylesheet', 'javascript', 'enable_comments',
        )
        widgets = {
            'body': MarkItUpTextarea,
            'stylesheet': CodeMirrorTextarea(**CSS_CODEMIRROR_ATTRS),
            'javascript': CodeMirrorTextarea(**JS_CODEMIRROR_ATTRS),
        }
    
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category