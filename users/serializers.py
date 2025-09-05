from rest_framework import serializers
from django.contrib.auth.models import User

from profiles.models import Profile
from profiles.serializers import ProfileSerializer


# Serializer to create users
class UserRegisterSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True)

  class Meta:
    model = User
    fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password']

    def create (self, validated_data):
      user = User.objects.create_user(
        username=validated_data['username'],
        email=validated_data.get('email'),
        first_name=validated_data.get('first_name', ''),
        last_name=validated_data.get('last_name', ''),
        password=validated_data['password']
      )
      Profile.objects.create(user=user)
      return user


# Serializer to show in the frontened
class UserListSerializer(serializers.ModelSerializer):
  profile = ProfileSerializer(read_only=True)

  class Meta:
    model = User
    fields = ['id', 'first_name', 'last_name', 'email', 'username', 'profile']
    read_only_fields = ['id']