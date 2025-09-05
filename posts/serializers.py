from django.contrib.auth.models import User
from rest_framework import serializers
from posts.models import Comment, Post
from users.serializers import UserListSerializer

class CommentSerializer(serializers.ModelSerializer):
  user = UserListSerializer()
  class Meta:
    model = Comment
    fields = [
      'post',
      'description',
      'publication_date',
      'user',
    ]
    read_only_fields = ['user']


class PostSerializer(serializers.ModelSerializer):
  comments = CommentSerializer(many=True, read_only=True)
  user = UserListSerializer(read_only=True)
  class Meta:
    model = Post
    fields = [
      'id',
      'title',
      'description',
      'publication_date',
      'user',
      'comments',
    ]