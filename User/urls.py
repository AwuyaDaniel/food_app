from django.urls import path

from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from . import views


app_name = 'UserProfile'


urlpatterns = [

    path('login_user', views.LoginView.as_view(), name='login'),
    path('register_user', views.UserCreateView.as_view(), name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('user/', views.get_user, name="user_profile"),
    path('users/', views.get_users, name="users"),
    path('users/<str:email>/', views.get_single_user, name="single_user"),
    path('deactivate_users/', views.deactivate, name="disable_user"),

]
