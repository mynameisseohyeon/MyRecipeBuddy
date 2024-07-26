from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

from postDetail import views as postDetail_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('main.urls')),
    path('postDetail/', include('postDetail.urls')),
    path('login/', include('login.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('comment/create/<int:content_id>/', postDetail_views.comment_create, name='comment_create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
