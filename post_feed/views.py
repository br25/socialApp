from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post, Comments, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer



class PostListView(APIView):
    def get(self, request):
        queryset = Post.objects.all()
        print(queryset)
        serializer = PostSerializer(queryset, many=True, context={'request': request})
        print(serializer)
        return Response(serializer.data)

    