from django.contrib import admin
from django.urls import path

from posts.views import CreateCommentView, DeleteCommentView, DeletePersonalPostView, EditCommentView, PersonalPostView, PostCreateView, PostListView, UpdatePersonalPostView
# from posts.views import CommentAPIListView, CommentDetailAPIView, CreateCommentView, DeleteCommentView, DeletePersonalPostView, EditCommentView, PersonalPostView, PostAPIListView, PostCreateView, PostDetailApiView, PostListView, UpdatePersonalPostView, comment_detail, comment_list, post_detail, post_list
# from posts.views import PersonalPostView, PostCreateView, addNewPost, editComment, editPost, myPosts, showAllPosts




urlpatterns = [
    # path("api/posts/", PostAPIListView.as_view(), name="posts_api"),
    # path("api/posts/<int:pk>/", PostDetailApiView.as_view(), name="posts_detail_api"),
    # path("api/comments/", CommentAPIListView.as_view(), name="comments_api"),
    # path("api/comments/<int:pk>/", CommentDetailAPIView.as_view(), name="comment_detail_api"),


    path('add-post/', PostCreateView.as_view(), name='add_post'),
    path('posts/', PostListView.as_view(), name='posts'),
    path("posts/<int:pk>/create-comment/", CreateCommentView.as_view(), name="create_comment"),
    path('my-posts/', PersonalPostView.as_view(), name='my_posts'),
    path('my-posts/edit-post/<int:pk>/', UpdatePersonalPostView.as_view(), name='edit_post'),
    path('my-posts/delete-post/<int:pk>/', DeletePersonalPostView.as_view(), name='delete_post'),
    path('posts/<int:post_id>/edit-comment/<int:pk>/', EditCommentView.as_view(), name='edit_comment'),
    path("posts/<int:post_id>/delete-comment/<int:pk>/", DeleteCommentView.as_view(), name="delete_comment")

]



# urlpatterns = [
#     path('add-post/', addNewPost, name='add_post'),
#     path('posts/', showAllPosts, name='posts'),
#     path('my-posts/', myPosts, name='my_posts'),
#     path('my-posts/edit-post/<int:pk>/', editPost, name='edit_post'),
#     path('posts/<int:post_id>/edit-comment/<int:comment_id>/', editComment, name='edit_comment'),

# ]