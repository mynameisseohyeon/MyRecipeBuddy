from django.shortcuts import render
from .models import MainContent

def postDetailPage(request):
    post_list = MainContent.objects.order_by('-pub_date')
    return render(request, 'pages/postDetailPage.html', {'post_list': post_list})
