from django.urls import path

from profiles.views import ProfileCreateView


urlpatterns = [
  path('create-profile/', ProfileCreateView.as_view(), name=''),
]
