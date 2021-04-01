from django.shortcuts import render, redirect, reverse
from django.views import View
from teachers.models import Teacher, Subject, SubjectTaughtBy
# Create your views here.


class Home(View):
    def get(self, request):
        context = {
            "teachers": Teacher.objects.all(),
            "subjects": Subject.objects.all(),
            "subjectTaughtBy": SubjectTaughtBy.objects.all()
        }
        return render(request, "index.html", context=context)

    def post(self, request):
        subject = request.POST.get("subject")
        lastnameParam = request.POST.get("lastname")
        print(subject, lastnameParam)

        if subject == '':
            filtered_teachers = Teacher.objects.filter(
                lastname__startswith=lastnameParam)
        else:
            subject = Subject.objects.get(pk=subject)

            teachers = Teacher.objects.filter(
                lastname__startswith=lastnameParam)

            teachers = SubjectTaughtBy.objects.filter(
                subject=subject, teacher__in=teachers).values('teacher')

            # print(teachers)
            filtered_teachers = []
            for t in teachers:
                for _, v in t.items():
                    filtered_teachers.append(Teacher.objects.get(pk=v))

        context = {
            'teachers': filtered_teachers,
            'subjectTaughtBy': SubjectTaughtBy.objects.all(),
            "subjects": Subject.objects.all(),
            'selected_sub': subject
        }
        return render(request, 'index.html', context=context)


class TeacherProfile(View):
    def get(self, request, teacherID):
        context = {
            "teacher": Teacher.objects.get(pk=teacherID),
            'subjectTaughtBy': SubjectTaughtBy.objects.all()
        }
        return render(request, "teacher.html", context=context)
