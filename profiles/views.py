from rest_framework.generics import RetrieveUpdateAPIView, RetrieveAPIView
from rest_framework import permissions
from profiles.models import Profile
from profiles.serializers import ProfileSerializer

class ProfileEditView(RetrieveUpdateAPIView):
  serializer_class = ProfileSerializer
  permission_classes = [permissions.IsAuthenticated]

  def get_object(self):
    profile, created = Profile.objects.get_or_create(user=self.request.user) # tuple
    return profile

class ProfileDetailtAPIView(RetrieveAPIView):
  serializer_class = ProfileSerializer
  permission_classes = [permissions.IsAuthenticated]

  def get_object(self):
    return self.request.user.profile