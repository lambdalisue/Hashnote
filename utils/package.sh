#!/bin/bash
#
# Package Install Shell
#
yes | pip install markdown whoosh Pygments PyYAML Akismet
yes | pip install django django-compress django-reversetag django-pagination
yes | pip install django-tagging
# Install from github
yes | pip install -e git://github.com/alisue/django-modify-history#egg=django-modify-history
yes | pip install -e git://github.com/alisue/django-markitup-widget#egg=django-markitup-widget
yes | pip install -e git://github.com/alisue/django-codemirror-widget#egg=django-codemirror-widget
yes | pip install -e git://github.com/alisue/django-qwert#egg=django-qwert
