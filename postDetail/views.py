from django.shortcuts import render, redirect
from .models import PostContent
from .forms import CommentForm 
from django.contrib.auth.decorators import login_required 

def postDetailPage(request):
    post_list = PostContent.objects.order_by('-pub_date')
    post_content = {'post_list': post_list}

    return render(request, 'pages/postDetailPage.html', post_content)

@login_required(login_url='postDetail:login') #비로그인 상태에서 댓글 작성 시 로그인 화면으로 이동
def comment_create(request, content_id): #댓글 기능
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