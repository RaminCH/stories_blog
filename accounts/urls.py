from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

app_name = 'accounts'

urlpatterns = [
    # path('',login, name='login'),
    path('login/',CustomLoginView.as_view(), name = 'login'),
    path('logout/',LogoutView.as_view(), name = 'logout'),
    # path('register/',register, name='register'),
    path('register/',CustomRegisterView.as_view(), name='register'),
    path('change-password/',change_password, name='change-password'),
    path('forget-password/',forget_password, name='forget-password'),
    path('reset-password/',reset_password, name='reset-password')
]