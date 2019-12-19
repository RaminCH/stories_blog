from django import forms 
from .models import *

class ContactForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Name'
    }) ,max_length = 20)
    email = forms.CharField(label='',widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Email'
    }) ,max_length = 20)
    subject = forms.CharField(label='',widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Subject'
    }) ,max_length = 1000)
    message = forms.CharField(label='',widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Your Message',
        'cols': '30',
        'rows': '7',
    }) ,max_length = 1000)

    # c = forms.CharField(label = 'bura c fieldidir', max_length = 20)

    class Meta:
        model = Contact
        fields = '__all__'
        # fields = ['message','c']

class CommentForm(forms.ModelForm):
    comment = forms.CharField(label='Your comment',widget=forms.Textarea(attrs={
        'class':'form-control',
    }))
    class Meta:
        model = Comment
        fields = ['comment',]