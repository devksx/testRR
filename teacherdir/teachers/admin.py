from django.contrib import admin
from teachers.models import Teacher, Subject, SubjectTaughtBy

admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(SubjectTaughtBy)
# Register your models here.
