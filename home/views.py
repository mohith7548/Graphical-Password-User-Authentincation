from django.shortcuts import render, HttpResponse


def home_page(request):
    return render(request, 'home.html')


def register_page(request):
    return HttpResponse('<h1> Register </h1>')


def login_page(request):
    return HttpResponse('<h1> Login </h1>')


def logout_page(request):
    return HttpResponse('<h1> Logout </h1>')