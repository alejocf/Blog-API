from django.contrib import admin
from django.urls import path

from posts.views import CommentAPIListView, CommentDetailAPIView, PostAPIListView, PostDetailApiView

urlpatterns = [
  path('posts/', PostAPIListView.as_view(), name=''),
  path('posts/<int:pk>/', PostDetailApiView.as_view(), name=''),
  path('comments/', CommentAPIListView.as_view(), name=''),
  path('comments/<int:pk>/', CommentDetailAPIView.as_view(), name=''),
]
