from rest_framework import serializers
from .models import Post, Comment, Like


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ["owner"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ["deleted_at"]


class PostSerializer(serializers.ModelSerializer):
    likes = LikeSerializer(many=True)
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        read_only_fields = ["deleted_at", "comments", "likes"]
        exclude = ["deleted_at"]

    def get_likes(self, obj):
        print(obj)
        likes = Like.objects.all().filter(post=obj)
        print(likes)
        return likes