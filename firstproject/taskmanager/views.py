from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from taskmanager.models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, 'taskmanager/index.html', {'tasks': tasks})
