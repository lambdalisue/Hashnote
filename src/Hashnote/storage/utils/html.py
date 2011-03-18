# -*- coding: utf-8 -*-
#
# Author:        alisue
# Date:            2010/11/28
#
from django.conf import settings
from django.template.defaultfilters import striptags
from django.utils.safestring import mark_safe

import os.path

def _image_viewer(url, thumbnail_url, title, description, width, height):
    kwargs = {
        'src': url,
        'thumbnail_src': thumbnail_url,
        'title': title,
        'description': description,
        'width': width,
        'height': height,
    }
    html = u"""
        <a href="%(src)s" rel="lightbox" title="%(title)s">
            <img src="%(thumbnail_src)s?width=%(width)s&height=%(height)s" alt="%(title)s" />
        </a>"""
    return mark_safe(html%kwargs)
def _audio_player(src, mimetype, width, height):
    kwargs = {
        'src': src,
        'mimetype': mimetype,
        'width': width,
        'height': height,
    }
    html = u"""
        <object type="%(mimetype)s" data="%(src)s" width="%(width)s" height="%(height)s" type="application/x-mplayer2">
            <param name="src" value="%(src)s" />
            <param name="autoplay" value="false" />
            <embed src="%(src)s" width="%(width)s" height="%(height)s" autoplay="false" type="application/x-mplayer2" />
        </object>"""
    return mark_safe(html%kwargs)
def _movie_player(src, mimetype, width, height):
    kwargs = {
        'src': src,
        'width': width,
        'height': height,
        'mimetype': mimetype,
    }
    if mimetype in ('video/x-flv', 'video/mp4'):
        kwargs['FLOWPLAYER'] = settings.MEDIA_URL + "component/flowplayer-3.2.5.swf"
        html = u"""
        <object id="flowplayer" width="%(width)s" height="%(height)s" data="%(FLOWPLAYER)s" 
            type="application/x-shockwave-flash"> 
            <param name="movie" value="%(FLOWPLAYER)s" /> 
            <param name="allowfullscreen" value="true" /> 
            <param name="flashvars" 
            value='config={"clip": {"url": "%(src)s", "autoPlay":false}}' />
        </object>"""
    elif mimetype in ('video/mpeg'):
        html = u"""
        <object data="%(src)s" width="%(width)s" height="%(height)s" type="video/mpeg">
            <param name="src" value="%(src)s" />
            <param name="autoplay" value="false" />
            <param name="autoStart" value="0" />
        </object>"""
    elif mimetype in ('video/x-msvideo', 'video/x-ms-wmv'):
        html = u"""
        <object data="%(src)s" width="%(width)s" height="%(height)s" type="%(mimetype)s">
            <param name="src" value="%(src)s" />from django.core.urlresolvers import reverse
            <param name="autoStart" value="0" />
        </object>"""
    return mark_safe(html%kwargs)
def _syntax_viewer(src, file, mimetype, width, height):
    # http://alexgorbatchev.com/SyntaxHighlighter/manual/brushes/
    SYNTAXES = {
        '.c':    'c',
        '.cs':   'csharp',
        '.cpp':  'cpp',
        '.css':  'css',
        '.js':   'javascript',
        '.java': 'java',
        '.pl':   'perl',
        '.php':  'php',
        '.py':   'python',
        '.rb':   'ruby',
        '.sql':  'sql',
        '.vb':   'vb',
        '.xml':  'xml',
        '.xhtml':'xhtml',
        '.sh':   'bash',
        '.html': 'html',
    }
    #try:
    buffer = file.readlines()
    buffer = "".join(buffer)
    ext = os.path.splitext(file.name)[1]
    kwargs = dict(
        syntax = SYNTAXES.get(ext, 'plain'),
        buffer = buffer,
        width = width,
        height = height,
    )
    return mark_safe(u"""<pre class="brush: %(syntax)s" width="%(width)s" height="%(height)s"
         style="display: block; overflow: scroll; width:%(width)spx; height: %(height)spx;">%(buffer)s</pre>"""%kwargs)
    #except:
    #    # Fail silently
    #    return _download_link(src, file, mimetype)
def _document_viewer(src, width, height):
    kwargs = {
        'src': src,
        'width': width,
        'height': height,
    }
    html = u"""<iframe src="http://docs.google.com/viewer?url=%(src)s&embedded=true" style="width:%(width)spx; height:%(height)spx;" frameborder="0"></iframe>"""
    return mark_safe(html % kwargs)
def _download_link(src, file, mimetype):
    def mtimg(mimetype):
        u"""mimetypeIconを出力する"""
        if mimetype:
            tag = r"""<span class="mtimg %s"></span>""" % " ".join(mimetype.split('/'))
        else:
            tag = r"""<span class="mtimg unknown"></span>"""
        return mark_safe(tag)
    def humanize(size):
        K = 1024
        M = K * K
        G = K * M
        if size >= G:
            return "%s GB" % round(float(size) / G, 2)
        elif size >= M:
            return "%s MB" % round(float(size) / M, 2)
        elif size >= K:
            return "%s KB" % round(float(size) / K, 2)
        return "%s byte" % size
    dict_info = dict(
        mtimg = mtimg(mimetype),
        src = src,
        title = os.path.basename(file.name),
        size = humanize(file.size)
    )
    return mark_safe(u"""%(mtimg)s <a href="%(src)s" title="%(title)s">%(title)s (%(size)s)</a>"""%dict_info)

def thumbnail_html(material, width, height):
    mimetype = material.mimetype
    filetype = material.filetype
    if filetype == 'image':
        return _image_viewer(
            url=material.get_preview_url(),
            thumbnail_url=material.get_thumbnail_url(),
            title=material.title,
            description=material.description,
            width=width,
            height=height,
        )
    elif filetype == 'audio':
        return _audio_player(
            src=material.get_preview_url(),
            mimetype=mimetype,
            width=width,
            height=height,
        )
    elif filetype == 'movie':
        return _movie_player(
            src=material.get_preview_url(),
            mimetype=mimetype,
            width=width,
            height=height,
        )
    elif filetype == 'text':
        if mimetype in ('application/vnd.ms-powerpoint', 'application/pdf'):
            return _document_viewer(
                src=material.get_preview_url(),
                width=width,
                height=height,
            )
        else:
            return _syntax_viewer(
                src=material.get_preview_url(),
                file=material.file,
                mimetype=mimetype,
                width=width,
                height=height,
            )
    else:
        return _download_link(
            src=material.get_download_url(),
            file=material.file,
            mimetype=mimetype,
        )