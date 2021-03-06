import datetime

from django.db import models
from django.core import urlresolvers

import tagging

# Create your models here.
class BlogEntryManager(models.Manager):
    def live(self):
        return self.all().filter(active=True)

class BlogEntry(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(help_text='The url name to use', unique=True)
    active = models.BooleanField(default=True)
    date = models.DateTimeField(default=datetime.datetime.now)

    body = models.TextField()

    objects = BlogEntryManager()

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('blog.views.blogentry_detail', (), {'slug':self.slug})

    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'blog entries'

tagging.register(BlogEntry)
