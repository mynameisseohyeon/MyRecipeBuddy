from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

# 사용자로부터 이메일과 비밀번호를 입력받음

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=60)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class SignupForm(UserCreationForm): 
    email = forms.EmailField() 
    class Meta: 
        model = User 
        fields = ("username", "password1", "password2", "email") 