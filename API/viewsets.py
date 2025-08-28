from rest_framework import viewsets
from rest_framework import permissions
from API.permissions import IsOwnerOrReadOnlyDetailAPIView
from API.serializers import CommentSerializer, PostSerializer
from posts.models import Comment, Post

class PostViewSet(viewsets.ModelViewSet):
  serializer_class = PostSerializer
  queryset = Post.objects.all()
  # permission_classes = [permissions.IsAuthenticated]
  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnlyDetailAPIView]

  def perform_create(self, serializer):
    serializer.save(user=self.request.user)

  def perform_update(self, serializer):
    serializer.save(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
  serializer_class = CommentSerializer
  queryset = Comment.objects.all()
  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnlyDetailAPIView]

  def perform_create(self, serializer):
    serializer.save(user=self.request.user)

  def perform_update(self, serializer):
    serializer.save(user=self.request.user)