
from gallery.models import *
from django.core.files import File

for i in range(8):
    gallery = Gallery(name='gallery-%s' % i, 
                      slug='gallery-%s' % i, 
                      description='lorem ipsum', 
                      thumbnail=File(open('assets/gallery_photo_thumbnail.jpg', 'rb')), 
                      tall_side_image=File(open('assets/gallery_tall_image.jpg', 'rb')))
    gallery.save()
    for j in range(10):
        photo = Photo(gallery=gallery,
                      thumbnail=File(open('assets/gallery_photo_thumbnail.jpg', 'rb')),
                      display=File(open('assets/gallery_photo_display.jpg', 'rb')))
        photo.save()

