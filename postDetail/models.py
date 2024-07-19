from django.db import models

# 장고는 SQL 작성없이 데이터 처리 가능
class PostContent(models.Model):
 title = models.CharField(max_length=200)
 content = models.TextField()
 pub_date = models.DateField('date published')