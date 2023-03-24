from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import EditForm, PostForm
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']


class ArticleView(DetailView):
    model = Post
    template_name = 'article.html'


class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'


class UpdatePost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update.html'


class DeletePost(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')


def CategoryView(requests, cats):
    category_post = Post.objects.filter(category=cats)
    return render(requests, 'categories.html', {'cats': cats, 'category_post': category_post})
