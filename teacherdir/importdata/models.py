from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class TeachersFile(models.Model):
    csvFile = models.FileField(upload_to='')
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def delete(self, *args, **kwargs):
        self.csvFile.delete()
        super().delete(*args, **kwargs)


class ZipProfileFile(models.Model):
    picZipFile = models.FileField(upload_to='')

    def delete(self, *args, **kwargs):
        self.picZipFile.delete()
        super().delete(*args, **kwargs)
