from django.contrib import admin
from django.urls import path, include

from taskmanager.views import index, by_category, TaskCreateView, delete

urlpatterns = [
    path('<int:category_id>/', by_category, name='by_category'),
    path('', index, name='index'),
    path('add/', TaskCreateView.as_view(), name='add'),
    path('delete/<int:task_id>', delete),
    path('edit/<int:task_id>', edit)
]

# репозиторий - папка
