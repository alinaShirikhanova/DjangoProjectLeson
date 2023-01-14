from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from taskmanager.models import Task, Category


def index(request):
    tasks = Task.objects.all()
    return render(request, 'taskmanager/index.html', {'tasks': tasks})


def by_category(request, category_id):
    tasks = Task.objects.filter(category=category_id)
    categories = Category.objects.all()
    current_category = Category.objects.get(pk=category_id)
    context = {'tasks': tasks, 'categories': categories, 'current_category': current_category}
    return render(request, 'taskmanager/by_category.html', context)
