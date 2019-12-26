from django import forms 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.forms import UsernameField
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm

User = get_user_model()


class CustomLoginForm(AuthenticationForm):
    username = UsernameField(label='', widget=forms.TextInput(attrs={
        'autofocus': True, 
        'class': 'form-control',
        'placeholder': "Username",
    }))
    password = forms.CharField(
        label='',
        strip=False, 
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': "Password",
        }),
    )

class CustomRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'Username'
    }))

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'First Name'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'Last Name'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder': 'Email'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder': 'Password'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder': 'Confirm Password'
    }))
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2',]


class CustomResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email',
    }), max_length=254)

class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'New password'
    }))
    
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm new password'
    }))
