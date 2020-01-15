from django.urls import path, re_path, include
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
    # path('reset-password/',reset_password, name='reset-password'),
    path('reset-password/', ReserPasswordView.as_view(), name='reset_password'),
    # path('password-reset-confirm/uidb64 token', ReserPasswordView.as_view(), name='password-reset-confirm')
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('api/', include('accounts.api.urls'))
]