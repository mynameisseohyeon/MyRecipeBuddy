# views.py 파일 (login 앱)
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm
from .forms import SignupForm 

def loginPage(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('mainpage')  # 로그인 성공 후 리디렉션할 URL 이름 사용
            else:
                messages.error(request, '이메일 또는 비밀번호가 틀립니다. 다시 시도해주세요.')
    else:
        form = LoginForm()

    return render(request, 'pages/loginPage.html', {'form': form})

def signup(request): 
    if request.method == "POST": 
        form = SignupForm(request.POST) 
        if form.is_valid(): 
            user = form.save() 
            login(request, user) 
            return redirect('/')  # 리디렉션을 들여쓰기를 맞춰서 if 블록 안으로 이동
    else: 
        form = SignupForm() 

    return render(request, 'pages/signup.html', {'form': form})
