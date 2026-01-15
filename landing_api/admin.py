from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "status", "priority", "owner", "created_at")
    list_filter = ("status", "priority")
    search_fields = ("title", "description", "owner__username")
