from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
from django.contrib import messages
from functools import wraps

def custom_login_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'Please login to create a post!')
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

@custom_login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')  
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})  

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'accounts/index.html', {'posts': posts})

def create_popup(request):
    return render(request, 'popup.html')    
