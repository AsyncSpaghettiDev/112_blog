from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)
from django.urls import path

urlpatterns = [
    path("", PostListView.as_view(), name="list"),
    path("create/", PostCreateView.as_view(), name="create"),
    path("<int:pk>/", PostDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", PostUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", PostDeleteView.as_view(), name="delete"),
]
