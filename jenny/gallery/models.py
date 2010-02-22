from django.db import models

# Create your models here.
class GalleryManager(models.Manager):
    def live(self):
        return self.all().filter(active=True)

class Gallery(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(help_text='The url name to use', unique=True)
    active = models.BooleanField(default=True, help_text='Uncheck to disable this gallery')
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='gallery-thumb', help_text='115x76 pixels')
    tall_side_image = models.ImageField(upload_to='gallery-thumb', help_text='116x358 pixels')
    order = models.IntegerField(default=0, help_text='Lower number goes first')

    objects = GalleryManager()

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('gallery.views.gallery_detail', (), {'slug':self.slug})

    class Meta:
        ordering = ['order']
        verbose_name_plural = 'galleries'

class Photo(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='photos')
    thumbnail = models.ImageField(upload_to='gallery-photos', help_text='115x76 pixels')
    display = models.ImageField(upload_to='gallery-photos', help_text='640x426 pixels')
    order = models.IntegerField(default=0, help_text='Lower number goes first')

    def __unicode__(self):
        return u'%s: Photo' % self.gallery

    class Meta:
        ordering = ['order']

