from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm, CommentForm
from django.contrib import messages
from functools import wraps
from django.shortcuts import get_object_or_404
from django.urls import reverse


def custom_login_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'message')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

@custom_login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')  
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})  


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                comment = form.save(commit=False)
                comment.post = post
                comment.author = request.user  
                comment.save()
                return redirect('post_detail', post_id=post_id)
            else:
                context = {
                    'message_text': 'You need to be logged in to comment.'
                }
                return render(request, 'message.html', context)

    return render(request, 'posts/post_detail.html', {'post': post, 'comments': comments, 'form': form})


