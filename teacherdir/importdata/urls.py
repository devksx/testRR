
from django.urls import path
from . import views

app_name = 'importdata'
urlpatterns = [
    path('', views.ImportData.as_view(), name='import-data'),
    path('clear-db', views.clearDb, name='clear-db')
]
