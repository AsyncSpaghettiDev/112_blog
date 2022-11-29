from .views import (
    HomePageView,
    AboutPageView,
    WeatherPageView,
)
from django.urls import path

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("weather/", WeatherPageView.as_view(), name="weather"),
]
