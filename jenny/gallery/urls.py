from django.conf.urls.defaults import *

from models import Gallery

gallery_qs = Gallery.objects.live()

urlpatterns = patterns('django.views.generic.list_detail',
    (r'^$', 'object_list', {'queryset':gallery_qs}, 'gallery.views.gallery_list'),
    (r'^(?P<slug>[\w\d-]+)/$', 'object_detail', {'slug_field':'slug', 'queryset':gallery_qs}, 'gallery.views.gallery_detail'),
)
