from django.contrib import admin
from django.urls import path, include
from .views import PostListView



urlpatterns=[
	path('', PostListView.as_view(), name='home'),
	# path('post/new/', views.create_post, name='post-create'),
	# path('post/<int:pk>/', views.post_detail, name='post-detail')
]