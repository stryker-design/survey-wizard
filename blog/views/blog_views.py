from django.shortcuts import render
from blog.models import BlogPost
from django.views.generic import ListView, DetailView, CreateView


# Create your views here.


class BlogView(ListView):
    model = BlogPost
    template_name = 'blog/blog-list.html'
    ordering = ['-id']

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog-detail.html'