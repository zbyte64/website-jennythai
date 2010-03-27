import datetime

from django.db import models
from django.core import urlresolvers

# Create your models here.
class BlogEntryManager(models.Manager):
    def tagged(self, tag):
        return self.all().filter(tags__ilike='%%s%%' % tag)

    def live(self):
        return self.all().filter(active=True)

class BlogEntry(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(help_text='The url name to use', unique=True)
    active = models.BooleanField(default=True)
    date = models.DateTimeField(default=datetime.datetime.now)
    tags = models.TextField(help_text='A comma seperated list of tags')

    body = models.TextField()

    objects = BlogEntryManager()

    def __unicode__(self):
        return self.title

    def tag_list(self):
        return self.tags.split(',')

    def tag_urls(self):
        for tag in self.tag_list():
            tag = tag.strip()
            yield tag, urlresolvers.reverse('blog.views.blogentrytag_list', args=(tag,))

    @models.permalink
    def get_absolute_url(self):
        return ('blog.views.blogentry_detail', (), {'slug':self.slug})

    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'blog entries'

#TODO media?

