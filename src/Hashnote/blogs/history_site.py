# -*- coding: utf-8 -*-
#
# Author:        alisue
# Date:            2011/02/23
#
from modify_history import site
from modify_history.backends.basic import BasicHistoryBackend

from models import Article

class ArticleBackend(BasicHistoryBackend):
    pass
site.register(Article, ArticleBackend)