from django.urls import path

from profiles.views import ProfileDetailtAPIView, ProfileEditView


urlpatterns = [
  path('edit-profile/', ProfileEditView.as_view(), name=''),
  path('my-profile/', ProfileDetailtAPIView.as_view(), name='')
]
