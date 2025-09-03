from posts.models import Comment, Post
from posts.permissions import IsOwnerOrReadOnlyDetailAPIView
from posts.serializers import CommentSerializer, PostSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework import permissions

# GET ALL POSTS
class PostAPIListView(ListAPIView):
  serializer_class = PostSerializer
  queryset = Post.objects.all()
  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnlyDetailAPIView]

# GET AND CREATE PERSONAL POSTS
class PersonalPostAPIListView(ListCreateAPIView):
  serializer_class = PostSerializer
  # permission_classes = [permissions.IsAuthenticated] # create more permissions

  def get_queryset(self):
    queryset = Post.objects.filter(user=self.request.user)
    return queryset

  def perform_create(self, serializer):
    serializer.save(user=self.request.user)

# POST DETAIL (PUT-DELETE POSTS)
class PostDetailApiView(RetrieveUpdateAPIView):
  allowed_methods = ['GET', 'PUT', 'DELETE']
  serializer_class = PostSerializer
  queryset = Post.objects.all()
  permission_classes = [IsOwnerOrReadOnlyDetailAPIView]

# GET ALL COMMENTS FOR EACH POST
class CommentAPIListView(ListAPIView):
  serializer_class = CommentSerializer
  queryset = Comment.objects.all()
  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnlyDetailAPIView]

  def perform_create(self, serializer):
    serializer.save(user=self.request.user)


# GET AND CREATE PERSONAL COMMENTS
class PersonalCommentAPIListView(ListCreateAPIView):
  serializer_class = CommentSerializer
  # permission_classes = [permissions.IsAuthenticated] # create more permissions

  def get_queryset(self):
    queryset = Comment.objects.filter(user=self.request.user)
    return queryset

  def perform_create(self, serializer):
    serializer.save(user=self.request.user)

# COMMENTS DETAIL (PUT-DELETE COMMENTS)
class CommentDetailAPIView(RetrieveUpdateAPIView):
  allowed_methods = ['GET', 'PUT', 'DELETE']
  serializer_class = CommentSerializer
  queryset = Comment.objects.all()
  permission_classes = [IsOwnerOrReadOnlyDetailAPIView]