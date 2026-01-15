from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    PRIORITY_CHOICES = [("LOW","LOW"), ("MEDIUM","MEDIUM"), ("HIGH","HIGH")]
    STATUS_CHOICES = [("TODO","TODO"), ("DOING","DOING"), ("DONE","DONE")]

    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default="LOW")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="TODO")
    due_date = models.DateField(null=True, blank=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.status})"
