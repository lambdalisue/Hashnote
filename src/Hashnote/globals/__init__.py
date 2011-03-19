# Make thees templatetags as builtins
from django.template import add_to_builtins
add_to_builtins('compress.templatetags.compressed')
add_to_builtins('reversetag.templatetags.reversetag')
add_to_builtins('pagination.templatetags.pagination_tags')
add_to_builtins('qwert.templatetags.markdown_tags')
