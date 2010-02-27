from django.test import TestCase
from django.utils.datastructures import MultiValueDict
from django.core.files.base import File
from django.conf import settings

from forms import GalleryForm

import os

class SimpleTest(TestCase):
    def test_basic_addition(self):
        from forms import flickr
        user = flickr.User('43513297@N03')
        photo_sets = user.getPhotosets()
        photo = photo_sets[0].getPhotos()[0]
        #print photo_sets[0].getPhotos()[0].getURL('Original', 'source')
        data = MultiValueDict({'name': 'test',
                               'slug': 'test',
                               'description': 'test',
                               'order':'1',
                               'thumbnail': 'thumbnail',
                               'tall_side_image': 'side_image'})
        data.setlist('photo_ids', [photo.id])
        test_photo = os.path.join(settings.PROJECT_DIR, 'jennytphotography_website-scale.jpg')
        files = {'thumbnail':File(open(test_photo, 'rb')),
                 'tall_side_image':File(open(test_photo, 'rb'))}
        form = GalleryForm(data, files)
        self.assertTrue(form.is_valid(), form.errors)
        gallery = form.save()
        self.assertTrue(gallery.photos.all().count())
        gallery.delete()


