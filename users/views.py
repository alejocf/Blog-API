from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from users.serializers import UserListSerializer, UserRegisterSerializer
from django.contrib.auth.models import User


class UserCreateView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserRegisterSerializer
  permission_classes = [AllowAny]

class UserAPIListView(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserListSerializer