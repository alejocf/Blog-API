from rest_framework import serializers

from posts.models import Comment, Post

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = '__all__'



class PostSerializer(serializers.ModelSerializer):
  comments = CommentSerializer(many=True, read_only=True)
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
