from django.shortcuts import render
# from .models import MainContent

# 페이지 제작 명령어 -> python manage.py startapp 페이지명
# django 실행 python manage.py runserver

# Create your views here.
def mainpage(request) :

  # 해당 content_list의 데이터를 다른 html파일에 적용 후 html을 리턴 가능(render함수)
  # mainpage_list = MainContent.objects.order_by('-pub_date')
  # content = {'mainpage_list': mainpage_list}

  return render(request, 'pages/mainpage.html')
