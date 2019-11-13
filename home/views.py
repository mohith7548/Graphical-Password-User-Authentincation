from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from graphical_pwd_auth.settings import N


def home_page(request):
    return render(request, 'home.html')


def register_page(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = User.objects.create_user(username=username, password=password)
        messages.success(request, 'Account created successfully!')
        return redirect('home')
    else:
        data = {
            'gpwd': [[False] * N] * N,
        }
        return render(request, 'register.html', context=data)


def login_page(request):
    return HttpResponse('<h1> Login </h1>')


def logout_page(request):
    return HttpResponse('<h1> Logout </h1>')