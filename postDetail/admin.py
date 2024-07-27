from django.contrib import admin
from .models import PostContent, Comment

# 관리자 페이지 개선 (가독성이 좋도록 수정)
class PostContentAdmin(admin.ModelAdmin): 
    list_display = ['title', 'content', 'pub_date'] 
    search_fields = ['title'] 

class CommentAdmin(admin.ModelAdmin): 
    list_display = ['content_list', 'content', 'author', 'create_date', 'modify_date'] 
    search_fields = ['author'] 

admin.site.register(PostContent, PostContentAdmin)
admin.site.register(Comment, CommentAdmin)