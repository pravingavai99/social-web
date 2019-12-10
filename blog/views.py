from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from users import views as user_views
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

def index(request):
    all_posts= Post.objects.order_by('-date_posted')
    return render(request, 'blog/home.html',{'all_posts': all_posts})


def about(request):
    return render(request, 'blog/about.html')
