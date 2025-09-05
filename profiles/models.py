from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
  profile_photo = models.ImageField(blank=True, null=True)
  bio = models.TextField(blank=True)
  instagram = models.URLField(blank=True, null=True)
  birthday = models.DateField(blank=True, null=True)
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

  def __str__(self):
    return f'Profile of {self.user.username}'
