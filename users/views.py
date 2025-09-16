from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from users.serializers import UserListSerializer, UserRegisterSerializer
from django.contrib.auth.models import User

# Create Account
class UserCreateView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserRegisterSerializer
  permission_classes = [permissions.AllowAny]

# List All Users
class UserAPIListView(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserListSerializer