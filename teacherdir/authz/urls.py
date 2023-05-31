
from django.urls import path
from . import views

app_name = 'authz'
urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.logout, name='logout')
]
