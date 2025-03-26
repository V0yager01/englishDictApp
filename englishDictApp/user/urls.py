from django.contrib import admin
from django.urls import path
from django.contrib.auth import views 

from . import views as view

app_name = 'user'

urlpatterns = [
    path('profile_page/', view=view.profile_page, name='profile'),
    path('register/', view=view.user_registration, name='signup'),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(next_page='user:login'), name="logout")
]