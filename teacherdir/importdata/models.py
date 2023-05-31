from django.db import models
from django.contrib.auth.models import User
from teachers.models import Teacher
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


# class ImageProfileFile(models.Model):
#     teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
#     image = models.ImageField(upload_to='media/', null=True
#                               default="https://bootdey.com/img/Content/avatar/avatar7.png")

#     def delete(self, *args, **kwargs):
#         self.image.delete()
#         super().delete(*args, **kwargs)
