from rest_framework import serializers
from .models import Post, Comments, Like

class PostSerializer(serializers.Serializer):
	id = serializers.IntegerField()
	owner = serializers.CharField(max_length=255)
	content = serializers.CharField(max_length=255)
	
   


class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comments
		fields = ['comment', 'post']



class LikeSerializer(serializers.ModelSerializer):
	id = serializers.IntegerField()
	post = serializers.CharField(max_length=255)

	