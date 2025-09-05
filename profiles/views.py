from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework import permissions
from profiles.serializers import ProfileSerializer

class ProfileEditView(RetrieveUpdateAPIView):
  serializer_class = ProfileSerializer
  permission_classes = [permissions.IsAuthenticated]

  def get_object(self):
    return self.request.user.profile
