from django.forms import ModelForm

from taskmanager.models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'category')
