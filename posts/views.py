from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "posts/list.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/detail.html"


class PostCreateView(CreateView):
    model = Post
    template_name = "posts/new.html"
    fields = ["title", "subtitle", "body"]
