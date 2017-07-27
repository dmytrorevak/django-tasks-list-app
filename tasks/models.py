from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    name = models.CharField(max_length=50, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=False)
    is_complete = models.BooleanField(default=False, blank=False)
    deadline = models.DateTimeField(blank=False)

    def __str__(self):
        return self.name
