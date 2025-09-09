from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework import permissions
from profiles.models import Profile
from profiles.serializers import ProfileSerializer

class ProfileEditView(RetrieveUpdateAPIView):
  serializer_class = ProfileSerializer
  permission_classes = [permissions.IsAuthenticated]

  def get_object(self):
    profile = Profile.objects.get_or_create(user=self.request.user)
    return profile
