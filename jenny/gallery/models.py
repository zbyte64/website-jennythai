from django.db import models
from sorl.thumbnail.fields import ThumbnailField

# Create your models here.
class GalleryManager(models.Manager):
    def live(self):
        return self.all().filter(active=True)

class Gallery(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(help_text='The url name to use', unique=True)
    active = models.BooleanField(default=True, help_text='Uncheck to disable this gallery')
    description = models.TextField()
    _display = ThumbnailField('display', upload_to='gallery-photos', size=(840,560), options=['crop'], db_column='display', blank=True)
    order = models.IntegerField(default=0, help_text='Lower number goes first')

    objects = GalleryManager()

    def __unicode__(self):
        return self.name

    def display(self):
        if self._display:
            return self._display
        return self.photos.all()[0].display

    @models.permalink
    def get_absolute_url(self):
        return ('gallery.views.gallery_detail', (), {'slug':self.slug})

    class Meta:
        ordering = ['order']
        verbose_name_plural = 'galleries'

class Photo(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='photos')
    thumbnail = ThumbnailField(upload_to='gallery-photos', help_text='115x77 pixels', size=(115,77), options=['crop'])
    display = ThumbnailField(upload_to='gallery-photos', help_text='840x560 pixels', size=(840,560), options=['crop'])
    order = models.IntegerField(default=0, help_text='Lower number goes first')

    def __unicode__(self):
        return u'%s: Photo' % self.gallery

    class Meta:
        ordering = ['order']

