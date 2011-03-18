# Make thees templatetags as builtins
from django.template import add_to_builtins
add_to_builtins('compress.templatetags.compressed')
add_to_builtins('reversetag.templatetags.reversetag')
add_to_builtins('pagination.templatetags.pagination_tags')
add_to_builtins('globals.templatetags.expr')
add_to_builtins('globals.templatetags.smart_if')
add_to_builtins('globals.templatetags.switchcase')
add_to_builtins('globals.templatetags.truncateletters')
add_to_builtins('globals.templatetags.markup_tags')

from django.conf import settings
from django.contrib.auth import models as auth_models
from django.contrib.auth.management import create_superuser
from django.db.models import signals

# From http://stackoverflow.com/questions/1466827/ --
#
# Prevent interactive question about wanting a superuser created.  (This code
# has to go in this otherwise empty "models" module so that it gets processed by
# the "syncdb" command during database creation.)
signals.post_syncdb.disconnect(
    create_superuser,
    sender=auth_models,
    dispatch_uid='django.contrib.auth.management.create_superuser')


# Create our own test user automatically.

def create_testuser(app, created_models, verbosity, **kwargs):
    if not settings.DEBUG:
        return
    try:
        auth_models.User.objects.get(username='admin')
    except auth_models.User.DoesNotExist:
        print '*' * 80
        print 'Creating test user -- login: admin, password: admin'
        print '*' * 80
        assert auth_models.User.objects.create_superuser('admin', 'x@x.com', 'admin')
    else:
        print 'Test user already exists. -- login: admin, password: admin'

signals.post_syncdb.connect(create_testuser,
    sender=auth_models, dispatch_uid='common.models.create_testuser')

#
# Protect Comment from Spam with Akismet
#
def on_comment_was_posted(sender, comment, request, *args, **kwargs):
    # spam checking can be enabled/disabled per the comment's target Model
    #if comment.content_type.model_class() != Entry:
    #    return

    from django.contrib.sites.models import Site
    from django.conf import settings

    try:
        from akismet import Akismet
    except:
        return

    # use TypePad's AntiSpam if the key is specified in settings.py
    if hasattr(settings, 'TYPEPAD_ANTISPAM_API_KEY'):
        ak = Akismet(
            key=settings.TYPEPAD_ANTISPAM_API_KEY,
            blog_url='http://%s/' % Site.objects.get(pk=settings.SITE_ID).domain
        )
        ak.baseurl = 'api.antispam.typepad.com/1.1/'
    else:
        ak = Akismet(
            key=settings.AKISMET_API_KEY,
            blog_url='http://%s/' % Site.objects.get(pk=settings.SITE_ID).domain
        )

    if ak.verify_key():
        data = {
            'user_ip': request.META.get('REMOTE_ADDR', '127.0.0.1'),
            'user_agent': request.META.get('HTTP_USER_AGENT', ''),
            'referrer': request.META.get('HTTP_REFERER', ''),
            'comment_type': 'comment',
            'comment_author': comment.user_name.encode('utf-8'),
        }

        if ak.comment_check(comment.comment.encode('utf-8'), data=data, build_data=True):
            if hasattr(comment.content_object,'author'):
                user = comment.content_object.author
            else:
                from django.contrib.auth.models import User
                user = User.objects.filter(is_superuser=True)[0]

            comment.flags.create(
                user=user,
                flag='spam'
            )
            comment.is_public = False
            comment.save()
from django.contrib.comments.signals import comment_was_posted
comment_was_posted.connect(on_comment_was_posted)
