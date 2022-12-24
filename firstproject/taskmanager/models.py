from django.db import models


class Task(models.Model):
    title = models.CharField('title', max_length=100)
    description = models.TextField('description', max_length=250)
    creation_time = models.DateTimeField(auto_now_add=True, db_index=True)
