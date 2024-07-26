from django.db import models
from django.utils import timezone

# 장고는 SQL 작성없이 데이터 처리 가능
# python manage.py makemigrations
# 실제 데이터베이스 모델에 적용하기 위한 python manage.py migrate

class LoginContent(models.Model):
 email = models.EmailField(max_length=60, unique=True)
 password = models.CharField(max_length=60)
 pub_date = models.DateTimeField(default=timezone.now) # pub_date 필드에 default 값을 추가