# -*- coding: utf-8 -*-
#
# Author:        alisue
# Date:            2011/01/01
#
__ALL__ = ['COMPRESS_CSS', 'COMPRESS_JS']

COMPRESS_CSS = {}
COMPRESS_JS = {}

def load_compress_settings():
    import os, imp, glob
    root = os.path.dirname(__file__)
    for path in glob.glob("%s/*.py" % root):
        filename = os.path.basename(path)
        if filename == '__init__.py': continue
        mod = imp.load_source(filename, path)
        COMPRESS_CSS.update(mod.COMPRESS_CSS)
        COMPRESS_JS.update(mod.COMPRESS_JS)
load_compress_settings()