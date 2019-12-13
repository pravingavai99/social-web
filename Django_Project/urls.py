from django.contrib import admin
from django.urls import include, path
from users import views as user_views  # from users app
from django.contrib.auth import views as auth_views  # models for login & logout

urlpatterns = [
    path('', include('blog.urls')),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('admin/', admin.site.urls),
    path(r'login/', auth_views.LoginView.as_view(template_name="users/login.html"),
         name="login"),
    path(r'logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"),
         name="logout"),

]
