
from django.urls import path
from . import views

app_name = 'teachers'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('teachers/', views.Home.as_view(), name='teachers'),
    path('teachers/<int:teacherID>',
         views.TeacherProfile.as_view(), name='teacher-profile')
]
