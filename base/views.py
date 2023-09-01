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

def search(request):
    query = request.GET.get('q')
    posts = []
    users = []

    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) | 
            Q(content__icontains=query)            
        )

        users = Profile.objects.filter(
            Q(user__username__icontains=query)
        )

    context = {
        'posts': posts,
        'users': users,
        'query': query
    }

    return render(request, 'search_results.html', context)        