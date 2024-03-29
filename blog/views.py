from django.shortcuts import render, get_object_or_404
from blog.models import Post

def  blog_view(request):
    
    posts = Post.objects.filter(status = 1)
    context ={'posts':posts}
    
    return render(request,'blog/blog-home.html',context=context)

def  single_view(request,pid):
    post = get_object_or_404(Post,pk=pid,status = 1)
    context ={'post':post}
    return render(request,'blog/blog-single.html',context=context)

def test(request,pid):
    # posts = Post.objects.all()
    # posts = Post.objects.get(id=pid)
    posts = get_object_or_404(Post,pk=pid)
    context ={'posts':posts}
    return render(request,'test.html',context=context)
