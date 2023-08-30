from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token

from . import views


from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', views.UsersViewSet)


urlpatterns = [
    path('users/', include(router.urls)),
    path('users/login', views.ApiLogin.as_view(), name='api_login'),
    path('users/register', views.UserRegistrationAPIView.as_view(), name='api_user_registration'),

]