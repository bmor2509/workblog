from django.db.models.query import QuerySet
from django.shortcuts import render
# Importing view templates 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Visibility
from .forms import PostForm, EditForm
# Create your views here.
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(ListView):

    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

    def get_queryset(self):
        if self.request.GET.get('fromdate')!= '' and self.request.GET.get('fromdate')!=None and self.request.GET.get('todate')!='' and self.request.GET.get('todate')!=None:
            from_date = self.request.GET.get('fromdate')
            to_date = self.request.GET.get('todate')
            site = self.request.GET.get('sites')
            self.queryset = Post.objects.all()
            return self.queryset.filter(post_date__gte=from_date).filter(post_date__lte=to_date).filter(site=site).order_by('-post_date')
        else:
            return Post.objects.all().order_by('-post_date').filter(visibility='Public')

class MyPosts(ListView):
    model = Post
    template_name = 'my_posts.html'
    ordering = ['-post_date']

    def get_queryset(self):
        if self.request.GET.get('fromdate')!= '' and self.request.GET.get('fromdate')!=None and self.request.GET.get('todate')!='' and self.request.GET.get('todate')!=None:
            from_date = self.request.GET.get('fromdate')
            to_date = self.request.GET.get('todate')
            site = self.request.GET.get('sites')
            self.queryset = Post.objects.all()
            return self.queryset.filter(post_date__gte=from_date).filter(post_date__lte=to_date).filter(site=site).order_by('-post_date')
        else:
            return Post.objects.all().order_by('-post_date')

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

class AddPostView(LoginRequiredMixin,CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

    def get_initial(self):
        return {'author': self.request.user}
    

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'

class DeletePostView(DeleteView):
    model = Post
    template_name='delete_post.html'
    success_url = reverse_lazy('home')
   