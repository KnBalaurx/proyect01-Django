from django.shortcuts import render
from django.http import HttpResponse


def display(request):
    f = '<h1>Bienvenido a la segunda app</h1>'
    return HttpResponse(f)

# Create your views here.
