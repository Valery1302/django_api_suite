from django.shortcuts import render
from landing_api.models import Task
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    tasks = []
    if request.user.is_authenticated:
        tasks = Task.objects.filter(owner=request.user).order_by("-created_at")[:10]

    return render(request, "homepage/index.html", {"tasks": tasks})
