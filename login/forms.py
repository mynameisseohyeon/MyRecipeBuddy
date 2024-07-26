from django import forms

# 사용자로부터 이메일과 비밀번호를 입력받음

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=60)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)