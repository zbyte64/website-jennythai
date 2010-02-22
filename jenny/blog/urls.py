from django.conf.urls.defaults import *

from models import BlogEntry

blog_qs = BlogEntry.objects.live()

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.list_detail.object_list', {'queryset':blog_qs}, 'blog.views.blogentry_list'),
    (r'^tag/(?P<tagname>[\w\d-]+)/$', 'blog.views.blogentrytag_list'),
    (r'^(?P<slug>[\w\d-]+)/$', 'django.views.generic.list_detail.object_detail', {'slug_field':'slug', 'queryset':blog_qs}, 'blog.views.blogentry_detail'),
)
