from rest_framework import viewsets

from posts.models import Comment, Post
from posts.serializers import CommentSerializer, PostSerializer

class PostViewSet(viewsets.ModelViewSet):
  serializer_class = PostSerializer
  queryset = Post.objects.all()

class CommentViewSet(viewsets.ModelViewSet):
  serializer_class = CommentSerializer
  queryset = Comment.objects.all()