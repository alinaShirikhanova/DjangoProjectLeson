from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from taskmanager.forms import TaskForm
from taskmanager.models import Task, Category


class TaskCreateView(CreateView):
    template_name = 'taskmanager/create_task.html'
    form_class = TaskForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


def index(request):
    tasks = Task.objects.all().order_by('id')
    categories = Category.objects.all()
    return render(request, 'taskmanager/index.html', {'tasks': tasks, 'categories':categories})


def by_category(request, category_id):
    tasks = Task.objects.filter(category=category_id)
    categories = Category.objects.all()
    current_category = Category.objects.get(pk=category_id)
    context = {'tasks': tasks, 'categories': categories, 'current_category': current_category}
    return render(request, 'taskmanager/by_category.html', context)


def delete(request, task_id):
    Task.objects.get(id=task_id).delete()
    return HttpResponseRedirect('/taskmanager')


# def edit(request, task_id):
#     task = Task.objects.get(id=task_id)
#     categories = Category.objects.all()
#     if request.method == 'POST':
#         task.title = request.POST.get('title')
#         task.description = request.POST.get('description')
#         # task.category = request.POST.get('category')
#         task.save()
#         return HttpResponseRedirect('/taskmanager')
#     return render(request, 'taskmanager/edit_task.html',
#                   {'task': task, 'categories': categories})
def edit(request, task_id):
    task = Task.objects.get(id=task_id)
    categories = Category.objects.all()
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        category = request.POST.get('category')
        task.category = Category.objects.get(name=category)
        task.save()
        return HttpResponseRedirect('/taskmanager')
    else:
        return render(request, 'taskmanager/edit_task.html', {'task': task, 'categories': categories})
