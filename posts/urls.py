from django.contrib import admin
from django.urls import path

from posts.views import addNewPost, editComment, editPost, myPosts, showAllPosts

urlpatterns = [
    path('add-post/', addNewPost, name='add_post'),
    path('posts/', showAllPosts, name='posts'),
    path('my-posts/', myPosts, name='my_posts'),
    path('my-posts/edit-post/<int:pk>/', editPost, name='edit_post'),
    path('posts/<int:post_id>/edit-comment/<int:comment_id>/', editComment, name='edit_comment'),

]