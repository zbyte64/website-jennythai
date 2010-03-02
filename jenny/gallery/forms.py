from django import forms
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_unicode
from django.core.files.uploadedfile import SimpleUploadedFile
import flickr
import urllib2

from models import Gallery, Photo

from django.conf import settings

flickr.API_KEY = settings.ADMINFILES_FLICKR_API_KEY

class MultipleValueField(forms.Field):
    hidden_widget = forms.MultipleHiddenInput
    widget = forms.SelectMultiple
    default_error_messages = {
        'invalid_choice': _(u'Select a valid choice. %(value)s is not one of the available choices.'),
        'invalid_list': _(u'Enter a list of values.'),
    }

    def clean(self, value):
        """
        Validates that the input is a list or tuple.
        """
        if self.required and not value:
            raise forms.ValidationError(self.error_messages['required'])
        elif not self.required and not value:
            return []
        if not isinstance(value, (list, tuple)):
            raise forms.ValidationError(self.error_messages['invalid_list'])
        new_value = [smart_unicode(val) for val in value]
        return new_value

class GalleryForm(forms.ModelForm):
    photo_ids = MultipleValueField(widget=forms.MultipleHiddenInput)

    class Meta:
        model = Gallery
    
    def upload_from_flickr(self, photo_ids):
        for photo_id in photo_ids:
            flickrphoto = flickr.Photo(photo_id)
            url = flickrphoto.getURL('Original', 'source')
            name = url.split('/')[-1]
            original = urllib2.urlopen(url).read()
            photo = Photo(gallery=self.instance)
            photo.display.save(name, SimpleUploadedFile(name, original), False)
            photo.thumbnail.save(name, SimpleUploadedFile('th_'+name, original), False)
            photo.save()

    def save(self, commit=True):
        self.instance = super(GalleryForm, self).save(commit)
        self.upload_from_flickr(self.cleaned_data['photo_ids'])
        return self.instance
        
