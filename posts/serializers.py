from django.contrib.auth.models import User
from rest_framework import serializers
from posts.models import Comment, Post
from users.serializers import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
  user = UserSerializer()
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
  user = UserSerializer(read_only=True)
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