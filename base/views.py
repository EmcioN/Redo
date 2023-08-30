from django.shortcuts import render, redirect
from posts.models import Post

def homepage(request):
    posts = Post.objects.all()    
    context = {
        'posts': posts
    }    
    return render(request, 'index.html', context)