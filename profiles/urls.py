from django.urls import path

from profiles.views import ProfileEditView


urlpatterns = [
  path('create-profile/', ProfileEditView.as_view(), name=''),
]
