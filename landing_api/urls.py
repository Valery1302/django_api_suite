from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LandingApiIndex, TaskViewSet

router = DefaultRouter()
router.register(r"tasks", TaskViewSet, basename="tasks")

urlpatterns = [
    path("index/", LandingApiIndex.as_view(), name="landing_api_index"),
    path("", include(router.urls)),
]
