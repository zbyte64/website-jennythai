# Create your views here.
from adminfiles import views

class FlickrView(views.FlickrView):
    template_name = 'gallery/uploader/flickr.html'
