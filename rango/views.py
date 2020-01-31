from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner ", about(request))

def about(request):
    return HttpResponse("Rango says here is the about page ")