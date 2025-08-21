from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from posts.forms import NewCommentForm, NewPostForm
from posts.models import Comment, Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DeleteView
from django.views.generic.edit import CreateView, UpdateView


# GENERAL POSTS
class PostListView(LoginRequiredMixin, ListView):
  model = Post
  template_name = 'show_posts.html'

  def get_queryset(self):
    return Post.objects.order_by('-id')

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["comments"] = Comment.objects.all()
      return context



class PostCreateView(LoginRequiredMixin, CreateView):
  model = Post
  template_name = 'add_post.html'
  fields = ['title', 'description']
  success_url = reverse_lazy('posts')

  def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)


# COMMENTS POSTS
class CreateCommentView(LoginRequiredMixin, CreateView):
  model = Comment
  fields = ['description']
  template_name = 'add_comment.html'
  success_url = reverse_lazy('posts')

  def form_valid(self, form):
      form.instance.user = self.request.user
      postInstance = Post.objects.get(pk=self.kwargs['pk'])
      form.instance.post = postInstance
      return super().form_valid(form)

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["post"] = Post.objects.get(pk=self.kwargs['pk'])
      return context



class EditCommentView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = Comment
  form_class = NewCommentForm
  template_name = 'edit_comment.html'
  success_url = reverse_lazy('posts')

  def test_func(self):
     comment = self.get_object()
     return comment.user == self.request.user

class DeleteCommentView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = Comment
  template_name = 'delete_comment.html'
  success_url = reverse_lazy('posts')

  def test_func(self):
    comment = self.get_object()
    return comment.user == self.request.user

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["comment"] = Comment.objects.get(pk=self.kwargs['pk'])
      return context



# PERSONAL POST
class PersonalPostView(LoginRequiredMixin, ListView):
  model = Post
  template_name = 'personal_posts.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["posts"] = Post.objects.filter(user=self.request.user)
      return context

class UpdatePersonalPostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = Post
  form_class = NewPostForm
  template_name = 'edit_post.html'
  success_url = reverse_lazy('my_posts')

  def test_func(self):
    post = self.get_object()
    return post.user == self.request.user

class DeletePersonalPostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = Post
  template_name = 'delete_post.html'
  success_url = reverse_lazy('my_posts')

  def test_func(self):
    post = self.get_object()
    return post.user == self.request.user

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["post"] = Post.objects.get(pk=self.kwargs['pk'])
      context["totalComment"] = len(Comment.objects.filter(post=self.kwargs['pk']))
      return context




# @login_required
# def showAllPosts(request):
#   posts = Post.objects.all()
#   comments = Comment.objects.all()

#   if request.method == 'POST':
#     action = request.POST['action']
#     if action == 'CREATE-COMMENT':
#       description = request.POST.get('comment_description')
#       if description is not None and description.strip() != "":
#         post_id = int(request.POST['post_id'])
#         post = Post.objects.get(pk=post_id)
#         user = request.user
#         Comment.objects.create(post=post, user=user, description=description)

#         comments = Comment.objects.all()
#         return render(request, 'show_posts.html', {
#           'posts': list(posts),
#           'comments': comments
#         })

#       else:
#         message = "Message can't be empty"
#         return render(request, 'show_posts.html', {
#           'posts': list(posts),
#           'comments': comments,
#           'message': message
#         })

#     if action == 'EDIT-COMMENT':
#       post_id = int(request.POST['post_id'])
#       comment_id = int(request.POST['comment_id'])
#       return redirect(f'{post_id}/edit-comment/{comment_id}/')

#     if action =='DELETE-COMMENT':
#       comment_id = int(request.POST['comment_id'])
#       commentToDelete = Comment.objects.get(pk=comment_id)
#       commentToDelete.delete()

#       posts = Post.objects.all()
#       comments = Comment.objects.all()
#       return render(request, 'show_posts.html', {
#         'posts': list(posts),
#         'comments': comments
#       })


#   else:
#     return render(request, 'show_posts.html', {
#       'posts': list(posts),
#       'comments': comments
#     })

# @login_required
# def addNewPost(request):
#   if request.method == 'POST':
#     form = NewPostForm(request.POST)
#     newPost = form.save(commit=False)
#     newPost.user = request.user
#     newPost.save()
#     return redirect('posts')

#   return render(request, 'add_post.html', {
#     'form': NewPostForm
#   })

# def myPosts(request):
#   user = request.user.id
#   post = Post.objects.filter(user=user)
#   if request.method == 'POST':
#     post_id = int(request.POST['post_id'])
#     action = request.POST['action']

#     if action == 'EDIT-POST':
#       return redirect(f'edit-post/{post_id}/')

#     if action == 'DELETE-POST':
#       postToDelete = Post.objects.get(pk=post_id, user=user)
#       postToDelete.delete()
#       message = 'POST has been succesfully deleted'
#       return render(request, 'personal_posts.html', {
#         'posts': list(post),
#         'message': message
#       })

#   else:
#     return render(request, 'personal_posts.html', {
#       'posts': list(post)
#     })

# def editPost(request, pk):
#   user = request.user.id
#   postToEdit = Post.objects.get(pk=pk, user=user)
#   form = NewPostForm(instance=postToEdit)

#   if request.method == 'POST':
#     form = NewPostForm(request.POST, instance=postToEdit)
#     if form.is_valid():
#       form.save()
#       return redirect('my_posts')

#   return render(request, 'edit_post.html', {
#     'form': form
#   })

# def editComment(request, post_id, comment_id):
#   user = request.user
#   post = Post.objects.get(pk=post_id)
#   comment = Comment.objects.get(pk=comment_id, user=user)

#   if request.method == 'POST':
#     commentToEdit = request.POST['newComment']
#     comment.description = commentToEdit
#     comment.save()
#     return redirect('posts')

#   return render(request, 'edit_comment.html', {
#     'post': post,
#     'comment': comment
#   })