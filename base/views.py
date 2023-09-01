from django.shortcuts import render, redirect
from posts.models import Post
from accounts.models import Profile
from django.db.models import Q


def homepage(request):
    posts = Post.objects.all()    
    context = {
        'posts': posts
    }    
    return render(request, 'index.html', context)

