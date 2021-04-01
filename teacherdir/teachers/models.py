from django.db import models
# Create your models here.


class Teacher(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    pic_url = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=25, unique=True)
    phoneNum = models.CharField(max_length=14, null=True)
    roomNum = models.CharField(max_length=4, null=True)

    def __str__(self):
        return 'Teacher Obj - {} {}'.format(self.firstname, self.lastname)


class Subject(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return 'Subject Obj - {}'.format(self.name)


class SubjectTaughtBy(models.Model):

    class Meta:
        unique_together = (('teacher', 'subject'),)

    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return 'SubjectTaughtBy Obj - {} by {}'.format(self.teacher, self.subject)
