from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.postDetailPage, name='postDetailPage'),
    path('comment/update/<int:comment_id>/', views.comment_update, name='comment_update'), 
    path('comment/delete/<int:comment_id>/', views.comment_delete, name='comment_delete'), 
]