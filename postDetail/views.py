from django.shortcuts import render, redirect
from .models import PostContent
from .forms import CommentForm 

def postDetailPage(request):
    post_list = PostContent.objects.order_by('-pub_date')
    post_content = {'post_list': post_list}

    return render(request, 'pages/postDetailPage.html', post_content)

def comment_create(request, content_id): 
    content_list = get_object_or_404(PostContent, pk=content_id) 
 
    if request.method == 'POST': 
        form = CommentForm(request.POST) 
        if form.is_valid(): 
            comment = form.save(commit=False) 
            comment.content_list = content_list 
            comment.author = request.user 
            comment.save() 
            return redirect('detail', content_id=content_list.id) 
    else: 
        form = CommentForm() 
        context = {'content_list': content_list, 'form': form} 
    return render(request, 'pages/postDetailPage.html', {'post_content': post_content})