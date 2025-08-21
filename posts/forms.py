from django import forms

from posts.models import Comment, Post

class NewPostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['title', 'description',]

class NewCommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['description']