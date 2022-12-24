from django.contrib import admin
from django.urls import path, include

from taskmanager.views import index

urlpatterns = [
    path('', index),
]

# репозиторий - папка
