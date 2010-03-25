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
    flickr_url = models.CharField(max_length=255)
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

