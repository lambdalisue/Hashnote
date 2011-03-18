#!/bin/bash
#
# Package Install Shell
#
yes | pip install markdown whoosh Pygments PyYAML Akismet
yes | pip install django django-compress django-reversetag django-pagination
yes | pip install django-modify-history django-markitup-widget django-codemirror-widget
