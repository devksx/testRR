from django.shortcuts import render, redirect, HttpResponse, reverse
from django.views import View
from django.contrib.auth.models import auth, User
from django.contrib import messages
# Create your views here.


class Login(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):

        email = request.POST['email']
        password = request.POST['password']
        username = User.objects.get(email=email.lower()).username
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            print("logged in ")
            if request.GET.get('next', "") != "":
                return redirect(request.GET['next'])
            return redirect(reverse('teachers:home'))
        else:
            messages.info(request, "invalid credentials")
            return redirect(reverse('authz:login'))


def logout(request):
    auth.logout(request)
    return redirect(reverse('teachers:home'))
