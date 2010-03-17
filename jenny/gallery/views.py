# Create your views here.
from adminfiles import views

class FlickrView(views.FlickrView):
    __name__ = 'flickrview'
    template_name = 'gallery/uploader/flickr.html'
