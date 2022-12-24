from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from taskmanager.models import Task


def index(request):
    template = loader.get_template('taskmanager/index.html')
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return HttpResponse(template.render(context, request))
