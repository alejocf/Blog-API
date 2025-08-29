from posts.models import Comment, Post
from posts.permissions import IsOwnerOrReadOnlyDetailAPIView
from posts.serializers import CommentSerializer, PostSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework import permissions

# API VIEWS USING CLASSES
class PostAPIListView(ListCreateAPIView):
  serializer_class = PostSerializer
  queryset = Post.objects.all()
  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnlyDetailAPIView]

  def perform_create(self, serializer):
    serializer.save(user=self.request.user)

class PostDetailApiView(RetrieveUpdateAPIView):
  allowed_methods = ['GET', 'PUT', 'DELETE']
  serializer_class = PostSerializer
  queryset = Post.objects.all()
  permission_classes = [IsOwnerOrReadOnlyDetailAPIView]


class CommentAPIListView(ListCreateAPIView):
  serializer_class = CommentSerializer
  queryset = Comment.objects.all()
  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnlyDetailAPIView]

  def perform_create(self, serializer):
    serializer.save(user=self.request.user)


class CommentDetailAPIView(RetrieveUpdateAPIView):
  allowed_methods = ['GET', 'PUT', 'DELETE']
  serializer_class = CommentSerializer
  queryset = Comment.objects.all()
  permission_classes = [IsOwnerOrReadOnlyDetailAPIView]
