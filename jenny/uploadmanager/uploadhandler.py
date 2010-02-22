from django.core.files.uploadhandler import FileUploadHandler
from django.core.files.uploadedfile import UploadedFile
from django.core.cache import cache

from models import TemporaryUploadFile

class UploadProgressCachedHandler(FileUploadHandler):
    """
    Tracks progress for file uploads.
    The http post request must contain a header or query parameter, 'X-Progress-ID'
    which should contain a unique string to identify the upload to be tracked.
    """

    def __init__(self, request=None):
        super(UploadProgressCachedHandler, self).__init__(request)
        self.progress_id = None
        self.cache_key = None

    def handle_raw_input(self, input_data, META, content_length, boundary, encoding=None):
        self.content_length = content_length
        if 'X-Progress-ID' in self.request.GET :
            self.progress_id = self.request.GET['X-Progress-ID']
        elif 'X-Progress-ID' in self.request.META:
            self.progress_id = self.request.META['X-Progress-ID']
        if self.progress_id:
            self.cache_key = "%s_%s" % (self.request.META['REMOTE_ADDR'], self.progress_id )
            cache.set(self.cache_key, {
                'length': self.content_length,
                'uploaded' : 0
            })

    def new_file(self, field_name, file_name, content_type, content_length, charset=None):
        pass

    def receive_data_chunk(self, raw_data, start):
        if self.cache_key:
            data = cache.get(self.cache_key)
            data['uploaded'] += self.chunk_size
            cache.set(self.cache_key, data)
        return raw_data
    
    def file_complete(self, file_size):
        pass

    def upload_complete(self):
        if self.cache_key:
            cache.delete(self.cache_key)

class TemporaryUploadFileMiddleware(object):
    def fetch_uploaded_file(self, request, key):
        try:
            return TemporaryUploadFile.objects.get(progress_id='%s_%s' % (request.META['REMOTE_ADDR'], key))
        except TemporaryUploadFile.DoesNotExist:
            return None

    def process_request(self, request):
        if request.POST:
            for name, key in zip(request.POST.getlist('_temporary_upload_file'),
                                 request.POST.getlist('_temporary_upload_file_key')):
                tuff = self.fetch_uploaded_file(request, key)
                if tuff:
                    request.FILES[name] = UploadedFile(tuff.uploaded_file.file, 
                                                       tuff.uploaded_file.name,
                                                       size=tuff.uploaded_file.size,)

    def process_response(self, request, response):
        if request.POST:
            for key in request.POST.getlist('_temporary_upload_file_key'):
                tuff = self.fetch_uploaded_file(request, key)
                if tuff:
                    tuff.delete()
        return response



