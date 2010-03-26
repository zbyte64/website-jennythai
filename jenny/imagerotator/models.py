from django.db import models

class Rotator(models.Model):
    key = models.CharField(max_length=20, unique=True)
    delay = models.PositiveIntegerField(default=5)
    
    def __unicode__(self):
        return self.key

class RotatorImage(models.Model):
    rotator = models.ForeignKey(Rotator, related_name='images')
    image = models.ImageField(upload_to='image-rotator')
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']

