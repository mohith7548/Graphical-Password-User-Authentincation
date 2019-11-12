from django.shortcuts import render, HttpResponse


def home_page(request):
    return HttpResponse('<h1> Hello World </h1>')