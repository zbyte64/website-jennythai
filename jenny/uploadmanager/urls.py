from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^upload-progress/$', 'uploadmanager.views.upload_progress'),
    (r'^upload-temporary-file/$', 'uploadmanager.views.upload_temporary_file'),
)

