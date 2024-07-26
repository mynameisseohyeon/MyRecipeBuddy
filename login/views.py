from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm
from .models import LoginContent

def loginPage(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('pages/mainpage.html')  # 로그인 성공 후 리디렉션할 URL
            else:
                messages.error(request, '이메일 또는 비밀번호가 틀립니다. 다시 시도해주세요.')
    else:
        form = LoginForm()

    return render(request, 'pages/loginPage.html', {'form': form})