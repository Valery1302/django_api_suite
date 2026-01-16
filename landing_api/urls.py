from django.urls import path, include
from .views import LandingAPI

urlpatterns = [
    #path('firebase/',views.LandingAPI.as_view(), name='landing-firebase'),
    path("index/", LandingAPI.as_view(), name="landing_api_index"),
]
