from django.shortcuts import redirect, render

from posts.forms import NewPostForm
from django.contrib.auth.decorators import login_required

from posts.models import Comment, Post

@login_required
def showAllPosts(request):
  posts = Post.objects.all()
  comments = Comment.objects.all()

  if request.method == 'POST':
    action = request.POST['action']
    if action == 'CREATE-COMMENT':
      description = request.POST.get('comment_description')
      if description is not None and description.strip() != "":
        post_id = int(request.POST['post_id'])
        post = Post.objects.get(pk=post_id)
        user = request.user
        Comment.objects.create(post=post, user=user, description=description)

        comments = Comment.objects.all()
        return render(request, 'show_posts.html', {
          'posts': list(posts),
          'comments': comments
        })

      else:
        message = "Message can't be empty"
        return render(request, 'show_posts.html', {
          'posts': list(posts),
          'comments': comments,
          'message': message
        })

    if action == 'EDIT-COMMENT':
      post_id = int(request.POST['post_id'])
      comment_id = int(request.POST['comment_id'])
      return redirect(f'{post_id}/edit-comment/{comment_id}/')

    if action =='DELETE-COMMENT':
      comment_id = int(request.POST['comment_id'])
      commentToDelete = Comment.objects.get(pk=comment_id)
      commentToDelete.delete()

      posts = Post.objects.all()
      comments = Comment.objects.all()
      return render(request, 'show_posts.html', {
        'posts': list(posts),
        'comments': comments
      })


  else:
    return render(request, 'show_posts.html', {
      'posts': list(posts),
      'comments': comments
    })

@login_required
def addNewPost(request):
  if request.method == 'POST':
    form = NewPostForm(request.POST)
    newPost = form.save(commit=False)
    newPost.user = request.user
    newPost.save()
    return redirect('posts')

  return render(request, 'add_post.html', {
    'form': NewPostForm
  })

def myPosts(request):
  user = request.user.id
  post = Post.objects.filter(user=user)
  if request.method == 'POST':
    post_id = int(request.POST['post_id'])
    action = request.POST['action']

    if action == 'EDIT-POST':
      return redirect(f'edit-post/{post_id}/')

    if action == 'DELETE-POST':
      postToDelete = Post.objects.get(pk=post_id, user=user)
      postToDelete.delete()
      message = 'POST has been succesfully deleted'
      return render(request, 'personal_posts.html', {
        'posts': list(post),
        'message': message
      })

  else:
    return render(request, 'personal_posts.html', {
      'posts': list(post)
    })

def editPost(request, pk):
  user = request.user.id
  postToEdit = Post.objects.get(pk=pk, user=user)
  form = NewPostForm(instance=postToEdit)

  if request.method == 'POST':
    form = NewPostForm(request.POST, instance=postToEdit)
    if form.is_valid():
      form.save()
      return redirect('my_posts')

  return render(request, 'edit_post.html', {
    'form': form
  })

def editComment(request, post_id, comment_id):
  user = request.user
  post = Post.objects.get(pk=post_id)
  comment = Comment.objects.get(pk=comment_id, user=user)

  if request.method == 'POST':
    commentToEdit = request.POST['newComment']
    comment.description = commentToEdit
    comment.save()
    return redirect('posts')

  return render(request, 'edit_comment.html', {
    'post': post,
    'comment': comment
  })