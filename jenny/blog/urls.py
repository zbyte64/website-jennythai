from django.conf.urls.defaults import *

from models import BlogEntry

blog_qs = BlogEntry.objects.live()

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.list_detail.object_list', {'queryset':blog_qs}, 'blog.views.blogentry_list'),
    (r'^tag/(?P<tag>[\w\d-]+)/$', 'tagging.views.tagged_object_list', {'queryset_or_model':blog_qs}, 'blog.views.blogentry_taglist'),
    (r'^(?P<slug>[\w\d-]+)/$', 'django.views.generic.list_detail.object_detail', {'slug_field':'slug', 'queryset':blog_qs}, 'blog.views.blogentry_detail'),
)
