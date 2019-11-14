from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from graphical_pwd_auth.settings import N
import random


def home_page(request):
    return render(request, 'home.html')


def register_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        try:
            user = User.objects.create_user(username=username, password=password)
            messages.success(request, 'Account created successfully!')
        except Exception:
            # print(e)
            messages.warning(request, 'Error while creating Account!')
        
        return redirect('home')
    else:
        images = random.sample(range(1, 50), N * N)
        print(images)
        p_images = []
        for i in range(0, N * N, 5):
            p_images.append(images[i:i+5])
        print(p_images)

        data = {
            'p_images': p_images,
        }
        return render(request, 'register.html', context=data)


def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(username=username, password=password, request=request)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successfull!')
            return redirect('home')
        else:
            messages.warning(request, 'Wrong credentials!')
            return redirect('login')
    else:
        images = random.sample(range(1, 50), N * N)
        print(images)
        p_images = []
        for i in range(0, N * N, 5):
            p_images.append(images[i:i+5])
        print(p_images)

        data = {
            'p_images': p_images,
        }
        return render(request, 'login.html', context=data)


def logout_page(request):
    logout(request)
    messages.warning(request, 'You\'ve been logged out!')
    return redirect('home')