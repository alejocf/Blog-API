from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from profiles.models import Profile
from profiles.serializers import ProfileSerializer

class ProfileCreateView(CreateAPIView):
  queryset = Profile.objects.all()
  serializer_class = ProfileSerializer

  def perform_create(self, serializer):
    serializer.save(user=self.request.user)
