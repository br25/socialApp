from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, DestroyAPIView, GenericAPIView
from rest_framework.response import Response
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer


class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    print(queryset.values())

class PostComments(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get(self, request, pk, *args, **kwargs):
        queryset = Comment.objects.all().filter(post_id=pk)

        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)

    def post(self, request, pk, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(post_id=pk)
        return Response(serializer.data)


class PostCommentDelete(DestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def delete(self, request, post_id, pk):
        queryset = self.get_object()
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LikePost(GenericAPIView):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
    def post(self, request, pk):
        current_user =  request.user
        like = self.get_queryset().filter(post_id=pk, owner_id=int(request.data.get('owner')))

        print(like)
        if len(like) == 0:
            serializer = self.get_serializer(data={"post_id": pk, "owner": int(request.data.get('owner'))})
            serializer.is_valid(raise_exception=True)
            serializer.save(post_id=pk)

            return Response("liked")
        else:
            for item in like:
                print(item)
                item.delete()

            return Response("unliked")