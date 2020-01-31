from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner  <a href=/rango/about/>Go to About</a>")

def about(request):
    return HttpResponse("Rango says here is the about page <a href=/rango/>Go to Index</a>")