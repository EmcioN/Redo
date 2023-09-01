from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from .models import Profile
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from posts.models import Post
from django.db.models import Q


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)            
            login(request, user)
            return redirect('home')
        else:
            for error in form.errors:
                print(error)
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')  

def edit_profile(request):
    if not hasattr(request.user, 'profile'):
        Profile.objects.create(user=request.user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile', user_id=request.user.id)

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    
    context = {
        'u_form': u_form,
        'p_form': p_form,
        
    }

    return render(request, 'edit_profile.html', context)

@login_required
def profile(request, user_id):
    profile_user = get_object_or_404(User, pk=user_id)
    user_posts = profile_user.post_set.all()  
    context = {
        'profile_user': profile_user,
        'user_posts': user_posts
    }
    return render(request, 'profile.html', context)

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