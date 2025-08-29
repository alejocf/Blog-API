from datetime import date
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()
  publication_date = models.DateField(default=date.today)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f'Post: "{self.title}" by {self.user.username}'


class Comment(models.Model):
  post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  description = models.TextField()
  publication_date = models.DateField(default=date.today)

  def __str__(self):
    return f'Comment: "{self.description}" by {self.user.username}'
