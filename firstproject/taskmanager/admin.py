from django.contrib import admin

from .models import Task, Category


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'creation_time', 'category')
    list_display_links = ('title', 'description', 'creation_time')
    search_fields = ('title', 'description')


admin.site.register(Task, TaskAdmin)
admin.site.register(Category)

