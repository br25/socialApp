from django.contrib import admin
from django.urls import path, include
from .views import PostList, PostDetail, PostComments, PostCommentDelete

urlpatterns = [
    path('posts', PostList.as_view(), name='posts'),
	path('posts/<int:pk>', PostDetail.as_view(), name='post-details'),
	path('posts/<int:pk>/comments', PostComments.as_view(), name='post-comments'),
    path('posts/<int:post_id>/comments/<int:pk>',
         PostCommentDelete.as_view(), name='delete comments')
]