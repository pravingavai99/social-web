from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from users import views as user_views

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='about'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'), #filtered posts
   # path('user/<str:username>/', UserPostListView.as_view(), name='user_post_list'),

]
