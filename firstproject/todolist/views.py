from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

def index(request):
    return HttpResponse('<h1>Здесь должно отображаться что-то</h1>')
