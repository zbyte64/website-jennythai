import datetime

from django.db import models

# Create your models here.
class TemporaryUploadFileManager(models.Manager):
    def purge_old(self):
        old = self.all().filter(timestamp__lte=datetime.datetime.now()-datetime.timedelta(days=1))
        for old_file in old:
            old.delete() #purge file

class TemporaryUploadFile(models.Model):
    progress_id = models.CharField(max_length=64, unique=True)
    timestamp = models.DateTimeField(default=datetime.datetime.now)
    uploaded_file = models.FileField(upload_to='uploadmanager/%Y/%m/%d')

    objects = TemporaryUploadFileManager()

    def __unicode__(self):
        return self.progress_id

    def transfer_file(self, bound_file_field, save=True):
        bound_file_field.save(self.uploaded_file.name, self.uploaded_file, save)
        self.uploaded_file.delete()
        self.delete()


