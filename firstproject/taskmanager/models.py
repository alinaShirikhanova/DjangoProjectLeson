from django.db import models


class Task(models.Model):
    title = models.CharField('title', max_length=100)
    description = models.TextField('description', max_length=250)
    creation_time = models.DateTimeField(auto_now_add=True, db_index=True)
    category = models.ForeignKey('Category', null=True, on_delete=models.PROTECT)
    status = models.BooleanField('status', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['title']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name

