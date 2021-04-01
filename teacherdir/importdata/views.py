from django.shortcuts import render, reverse, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from importdata.models import TeachersFile, ZipProfileFile
from teachers.models import Teacher, Subject, SubjectTaughtBy
from django.db.utils import IntegrityError
from django.contrib import messages
import csv
from zipfile import ZipFile
# Create your views here.


@method_decorator(login_required, name="dispatch")
class ImportData(View):

    def get(self, request):
        return render(request, "import-form.html")

    def post(self, request):
        # for file in request.FILES:
        #     print(file)
        csv_file = request.FILES.get('csv-file')
        pics_file = request.FILES.get('pics-file')

        if csv_file != None and csv_file.name.endswith('.csv'):

            teacherFile = TeachersFile(csvFile=csv_file, user=request.user)
            teacherFile.save()
            with open(teacherFile.csvFile.path, 'r') as teacher_csv:
                reader = csv.DictReader(teacher_csv)
                try:
                    for line in reader:
                        if not (line['First Name'] == '' and line['Last Name'] == '' and line['Email Address'] == ''):

                            # print(line)
                            try:
                                current_teacher, isTCreated = Teacher.objects.get_or_create(
                                    email=line['Email Address']
                                )
                                current_teacher.firstname = line['First Name']
                                current_teacher.lastname = line['Last Name']
                                current_teacher.save()
                            except Exception as error:
                                print(error.__class__)

                            for subject in line['Subjects taught'].split(', '):
                                # print(subject.title())
                                try:
                                    subject, isSubCreated = Subject.objects.get_or_create(
                                        name=subject.title())
                                    subject.save()

                                    if len(SubjectTaughtBy.objects.filter(teacher=current_teacher)) < 5:
                                        stby = SubjectTaughtBy.objects.create(
                                            teacher=current_teacher,
                                            subject=subject
                                        )
                                        stby.save()
                                except IntegrityError:
                                    continue

                            if line['Profile picture'] != '':
                                current_teacher.pic_url = line['Profile picture']

                            if line['Phone Number'] != '':
                                current_teacher.phoneNum = line['Phone Number']

                            if line['Room Number'] != '':
                                current_teacher.roomNum = line['Room Number']

                            current_teacher.save()
                            # print(line)
                except KeyError:
                    messages.error(
                        request, "seems like you have choosen wrong csv file")
                    teacherFile.delete()
                    return redirect(reverse('importdata:import-data'))

                messages.info(request, "file successfully imported!")
            teacherFile.delete()

        if pics_file != None and pics_file.name.endswith('.zip'):
            print(pics_file.name)
            zipProfileFile = ZipProfileFile.objects.create(
                picZipFile=pics_file)
            zipProfileFile.save()
            with ZipFile(zipProfileFile.picZipFile.path, 'r') as zipFileObj:
                zipFileObj.extractall('media/')

            zipProfileFile.delete()

        return redirect(reverse('importdata:import-data'))


def clearDb(request):
    if request.method == "POST":
        Teacher.objects.all().delete()
        Subject.objects.all().delete()
        SubjectTaughtBy.objects.all().delete()
        messages.success(request, "successfully cleared database")
        return redirect(reverse('teachers:home'))
