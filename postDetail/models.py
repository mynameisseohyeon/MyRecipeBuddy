from django.db import models
from django.contrib.auth.models import User 

class PostContent(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateField('date published')
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)

    def __str__(self):
        return self.title
   


# 댓글 기능 추가
class Comment(models.Model): 
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    content_list = models.ForeignKey(PostContent, on_delete=models.CASCADE) 
    content = models.TextField() 
    create_date = models.DateTimeField(auto_now_add=True) 
    modify_date = models.DateTimeField(auto_now=True)