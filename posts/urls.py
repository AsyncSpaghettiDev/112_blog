from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
)
from django.urls import path

urlpatterns = [
    path("", PostListView.as_view(), name="list"),
    path("create/", PostCreateView.as_view(), name="create"),
    path("<int:pk>/", PostDetailView.as_view(), name="detail"),
]
