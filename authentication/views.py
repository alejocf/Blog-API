from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def createAccountView(request):
  if request.method == 'POST':
    username = request.POST['username']
    password1 = request.POST['password1']
    password2 = request.POST['password2']

    if password1 == password2:
      user = User.objects.create_user(username=username, password=password1)
      user.save()
      return redirect('login')
  else:
    return render(request, 'create_account.html', {
        'form': UserCreationForm,
        'errors': 'Paswords do not match'
    })

def loginView(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None:
      login(request, user)
      return redirect('posts')
      # breakpoint()
      # return print('User has been logued')

    else:
      error = "User doesn't exist"
      return render(request, 'login.html', {
        'form': AuthenticationForm,
        'errors': error
      })
  else:
    return render(request, 'login.html', {
      'form': AuthenticationForm,
    })

def logoutView(request):
  logout(request)
  return redirect('login')