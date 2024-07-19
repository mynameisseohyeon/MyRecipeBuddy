from django.shortcuts import render

# 페이지 제작 명령어 -> python manage.py startapp 페이지명
# django 실행 python manage.py runserver

# Create your views here.
def mainpage(request) :
 return render(request, 'pages/mainpage.html')
