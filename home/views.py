from django.shortcuts import render, HttpResponse
from graphical_pwd_auth.settings import N


def home_page(request):
    return render(request, 'home.html')


def register_page(request):

    if request.method == 'POST':
        return HttpResponse('posted')
    else:
        data = {
            'gpwd': [[False] * N] * N,
        }
        return render(request, 'register.html', context=data)


def login_page(request):
    return HttpResponse('<h1> Login </h1>')


def logout_page(request):
    return HttpResponse('<h1> Logout </h1>')