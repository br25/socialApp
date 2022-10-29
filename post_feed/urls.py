from django.contrib import admin
from django.urls import path, include
from .views import PostList, PostDetail

urlpatterns = [
    path('posts', PostList.as_view(), name='posts'),
	path('posts/<int:pk>', PostDetail.as_view(), name='post-details'),
]