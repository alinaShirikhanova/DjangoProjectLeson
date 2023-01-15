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
    tasks = Task.objects.all()
    return render(request, 'taskmanager/index.html', {'tasks': tasks})


def by_category(request, category_id):
    tasks = Task.objects.filter(category=category_id)
    categories = Category.objects.all()
    current_category = Category.objects.get(pk=category_id)
    context = {'tasks': tasks, 'categories': categories, 'current_category': current_category}
    return render(request, 'taskmanager/by_category.html', context)


def delete(request, task_id):
    Task.objects.get(id=task_id).delete()
    return HttpResponseRedirect('/taskmanager')


