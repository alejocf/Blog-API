from rest_framework import generics
from rest_framework import permissions
from profiles.models import Profile
from profiles.serializers import ProfileSerializer
from users.serializers import UserListSerializer

# Edit Profile (profile_photo, bio, instagram, birthday)
class ProfileEditView(generics.RetrieveUpdateAPIView):
  serializer_class = ProfileSerializer
  permission_classes = [permissions.IsAuthenticated]

  def get_object(self):
    profile, created = Profile.objects.get_or_create(user=self.request.user) # tuple
    return profile

# Read User And Profile (Detail)
class ProfileDetailtAPIView(generics.RetrieveAPIView):
  serializer_class = UserListSerializer
  permission_classes = [permissions.IsAuthenticated]

  def get_object(self):
    return self.request.user