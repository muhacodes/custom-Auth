from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('users', views.getAllUsers.as_view()),
    path('users/login', views.ApiLogin.as_view(), name='api_login'),
]