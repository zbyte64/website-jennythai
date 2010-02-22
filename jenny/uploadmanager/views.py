# Create your views here.from django.core.cache import cache
import random
import string

from django.http import HttpResponse, HttpResponseServerError
from django.utils import simplejson
from django.core.cache import cache

from models import TemporaryUploadFile
from uploadhandler import UploadProgressCachedHandler

def upload_progress(request):
    """
    Return JSON object with information about the progress of an upload.
    """
    progress_id = ''
    if 'X-Progress-ID' in request.GET:
        progress_id = request.GET['X-Progress-ID']
    elif 'X-Progress-ID' in request.META:
        progress_id = request.META['X-Progress-ID']
    if progress_id:
        cache_key = "%s_%s" % (request.META['REMOTE_ADDR'], progress_id)
        data = cache.get(cache_key)
        return HttpResponse(simplejson.dumps(data))
    else:
        return HttpResponseServerError('Server Error: You must provide X-Progress-ID header or query param.')

def upload_temporary_file(request):
    if request.method in ('POST', 'PUT'):
        ret = dict()
        for key, value in request.FILES.items():
            progress_id = ''.join([random.choice(string.letters + string.digits) for i in range(32)])
            cache_key = "%s_%s" % (request.META['REMOTE_ADDR'], progress_id)
            tuf = TemporaryUploadFile(progress_id=cache_key)
            tuf.uploaded_file.save(value.name, value)
            ret[key] = {'key':progress_id,
                        'name':value.name}
        return HttpResponse(simplejson.dumps(ret))
    return HttpResponseServerError('Must be a post')
