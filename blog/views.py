from django.shortcuts import render
from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView,
                                    DetailView, CreateView,
                                    UpdateView, DeleteView)
# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post

    ''' Returns  the list of views for this View'''
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).orderby('-published_date')  #__lte is less than equals too!

class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = '/blog/post_detail'
    form_class = PostForm
    model = Post

class UpdatePostView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = '/blog/post_detail'
    form_class = PostForm
    model = Post

class DeletePostView(LoginRequiredMixin,DetailView):
    model = Post
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list'
    model = Post

    def get_queryset(self):
        return Post.objects.self.filter(published_date__isnull=True).orderby('created_date')
