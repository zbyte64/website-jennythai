from django import forms
import flickr

from models import Gallery

from django.conf import settings

flickr.API_KEY = settings.ADMINFILES_FLICKR_API_KEY

class GalleryForm(forms.ModelForm):
    flickr_url = forms.ChoiceField(required=False)
    url_pattern = 'http://api.flickr.com/services/feeds/photoset.gne?set=%s&nsid=%s&lang=en-us&format=json'

    class Meta:
        model = Gallery

    def __init__(self, *args, **kwargs):
        super(GalleryForm, self).__init__(*args, **kwargs)
        user = flickr.User(id=settings.FLICKR_USER_ID)
        choices = list()
        for photoset in user.getPhotosets():
            choices.append((photoset.title, self.url_pattern % (photoset.id, user.id)))
        self.fields['flickr_url'].choices = choices
    
    def save_m2m(self):
        return
        
