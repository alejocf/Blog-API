from django.contrib import admin
from django.urls import include, path

from authentication.views import createAccountView, loginView, logoutView

urlpatterns = [
  path('create-account/', createAccountView, name='create_account'),
  path('login/', loginView, name='login'),
  path('logout/', logoutView, name='logout')
]