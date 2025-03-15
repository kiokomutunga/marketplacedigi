from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class loginForm(AuthenticationForm):
     username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'your username',
        'class': 'w-full py-4 px-6 roundend-xl'
    }))  
     password = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Password',
        'class': 'w-full py-4 px-6 roundend-xl'
    }))
class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields = ('username', 'email', 'password1','password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'your username',
        'class': 'w-full py-4 px-6 roundend-xl'
    }))    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter email',
        'class': 'w-full py-4 px-6 roundend-xl'
    }))    
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Password',
        'class': 'w-full py-4 px-6 roundend-xl'
    }))
    password2 = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'confirm email',
        'class': 'w-full py-4 px-6 roundend-xl'
    }))   