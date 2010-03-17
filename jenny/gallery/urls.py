from django.conf.urls.defaults import *
from django.contrib.admin.views.decorators import staff_member_required

from models import Gallery
from views import FlickrView

gallery_qs = Gallery.objects.live()
context = {
    'galleries':gallery_qs
}

urlpatterns = patterns('django.views.generic.list_detail',
    (r'^$', 'object_list', {'queryset':gallery_qs, 'extra_context':context}, 'gallery.views.gallery_list'),
    (r'^select/$', staff_member_required(FlickrView())),
    (r'^(?P<slug>[\w\d-]+)/$', 'object_detail', {'slug_field':'slug', 'queryset':gallery_qs, 'extra_context':context}, 'gallery.views.gallery_detail'),
)
