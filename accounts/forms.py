from django import forms 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.forms import UsernameField
from django.contrib.auth import get_user_model

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
    username = UsernameField(widget=forms.TextInput(attrs={
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

    email = forms.CharField(widget=forms.TextInput(attrs={
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