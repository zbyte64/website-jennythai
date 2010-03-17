from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.simple.direct_to_template', {'template':'index.html'}),
    (r'^bio/$', 'django.views.generic.simple.direct_to_template', {'template':'bio.html'}),
    (r'^booking/$', 'django.views.generic.simple.direct_to_template', {'template':'booking.html'}),
    (r'^contact/$', 'django.views.generic.simple.direct_to_template', {'template':'contact.html'}),
    #(r'^portfolio/$', 'django.views.generic.simple.direct_to_template', {'template':'portfolio.html'}),
    (r'^reviews/$', 'django.views.generic.simple.direct_to_template', {'template':'reviews.html'}),
    (r'^uploadmanager/', include('uploadmanager.urls')),
    (r'^blog/', include('blog.urls')),
    (r'^portfolio/', include('gallery.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    url(r'^adminfiles/', include('adminfiles.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )
