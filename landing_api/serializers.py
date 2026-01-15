from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    owner_username = serializers.CharField(source='owner.username', read_only=True)

    class Meta:
        model = Task
        fields = [
            "id", "title", "description", "priority", "status",
            "due_date", "owner", "owner_username", "created_at"
        ]
        read_only_fields = ["id", "owner", "created_at"]
