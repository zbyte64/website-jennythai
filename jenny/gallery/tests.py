from django.test import TestCase
from django.utils.datastructures import MultiValueDict
from django.core.files.base import File
from django.conf import settings

from forms import GalleryForm

import os

class SimpleTest(TestCase):
    def test_basic_addition(self):
        form = GalleryForm()
        self.assertTrue(form.fields['flickr_url'].choices)
        unicode(form)

