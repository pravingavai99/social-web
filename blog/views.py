from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def index(request):
    all_posts= Post.objects.order_by('-date_posted')
    return render(request, 'blog/home.html',{'all_posts': all_posts})

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'all_posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title','content']
    def form_valid(self, form):
        form.instance.author= self.request.user #current user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']
    def form_valid(self, form):
        form.instance.author= self.request.user #current user
        return super().form_valid(form)

    def test_func(self):
        post= self.get_object() #current post access
        if self.request.user==post.author:
            return True
        return False

class PostDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html')
