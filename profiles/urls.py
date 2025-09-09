from django.urls import path

from profiles.views import ProfileEditView


urlpatterns = [
  path('edit-profile/', ProfileEditView.as_view(), name=''),
  # path("profiles/", ProfileListAPIView.as_view(), name="")
]
