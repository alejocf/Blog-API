from django.contrib import admin
from django.urls import path

from posts.views import CommentAPIListView, CommentDetailAPIView, PersonalCommentAPIListView, PersonalPostAPIListView, PostAPIListView, PostDetailApiView

urlpatterns = [
  path('my-posts/', PersonalPostAPIListView.as_view(), name=''),
  path('posts/', PostAPIListView.as_view(), name=''),
  path('posts/<int:pk>/', PostDetailApiView.as_view(), name=''),
  path('my-comments/', PersonalCommentAPIListView.as_view(), name=''),
  path('comments/', CommentAPIListView.as_view(), name=''),
  path('comments/<int:pk>/', CommentDetailAPIView.as_view(), name=''),
]
