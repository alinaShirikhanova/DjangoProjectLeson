from django.db import models


class Forum(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(null=True, blank=True)
    creation_time = models.DateTimeField(auto_now_add=True, db_index=True)

