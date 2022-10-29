from rest_framework import serializers
from .models import Post, Comment, Like


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "owner", "post"


class PostSerializer(serializers.ModelSerializer):
    likes = LikeSerializer(many=True)

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ["deleted_at", "comments", "likes"]

    def get_likes(self, obj):
        print(obj)
        likes = Like.objects.all().filter(post=obj)
        print(likes)
        return likes


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ["deleted_at", "post"]