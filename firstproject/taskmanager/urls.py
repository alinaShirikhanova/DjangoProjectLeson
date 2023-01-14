from django.contrib import admin
from django.urls import path, include

from taskmanager.views import index, by_category

urlpatterns = [
    path('<int:category_id>/', by_category),
    path('', index, name='index'),
]

# репозиторий - папка
