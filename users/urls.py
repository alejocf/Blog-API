from django.urls import path

from posts.views import PersonalPostAPIListView
from users.views import UserAPIListView, UserCreateView


urlpatterns = [
  path('create-account/', UserCreateView.as_view(), name=''),
  path('users/', UserAPIListView.as_view(), name=''),
]
