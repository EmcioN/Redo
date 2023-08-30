from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [    

    path('create/', login_required(views.create_post), name='create_post'),
    path('create-popup/', views.create_popup, name='create_popup'),
    
]