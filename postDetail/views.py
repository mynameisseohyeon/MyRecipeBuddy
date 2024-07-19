from django.shortcuts import render
from .models import PostContent

def postDetailPage(request):
    post_list = PostContent.objects.order_by('-pub_date')
    post_content = {'post_list': post_list}

    return render(request, 'pages/postDetailPage.html', post_content)
