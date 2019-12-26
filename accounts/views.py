from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm, CustomRegisterForm, CustomResetPasswordForm, CustomSetPasswordForm
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView, PasswordResetForm, PasswordResetConfirmView

User = get_user_model() #when required to write custom user tools

# Create your views here.


def change_password(request):
    return render(request, 'change_password.html')

def forget_password(request):
    return render(request, 'forget_password.html')

# def login(request):
#     return render(request, 'login.html')
class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = CustomLoginForm
    

# def register(request):
#     return render(request, 'register.html')
class CustomRegisterView(CreateView):
    model = User
    template_name = 'register.html'
    # fields = '__all__'
    form_class = CustomRegisterForm
    success_url = reverse_lazy('accounts:login')


def reset_password(request):
    return render(request, 'reset_password.html')


class ReserPasswordView(PasswordResetView):
    form_class = CustomResetPasswordForm
    template_name = 'forget_password.html'
    email_template_name = 'password_reset_email.html'
    success_url = reverse_lazy('stories:index')

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'reset_password.html'
    form_class = CustomSetPasswordForm
    success_url = reverse_lazy('accounts:login')

