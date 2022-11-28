from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)


class PostListView(ListView):
    model = Post
    template_name = "posts/list.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/detail.html"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "posts/new.html"
    fields = ["title", "subtitle", "body", "status"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "posts/edit.html"
    fields = ["title", "subtitle", "body", "status"]

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "posts/delete.html"
    success_url = reverse_lazy("list")

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author
