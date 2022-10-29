from django.contrib import admin
from django.urls import path, include
from .views import PostList

urlpatterns = [
    path('posts', PostList.as_view(), name='posts'),
]