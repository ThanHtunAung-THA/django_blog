from django.shortcuts import render, redirect, get_object_or_404
from blog.models import PostModel
from django.contrib import messages
import datetime

# Create your views here.
# view
def post_list(request):
  # posts = PostModel.objects.all().order_by('-created_at')
  posts = PostModel.objects.all().order_by('-created_at')
  return render(request, 'postList.html', {"posts" : posts})

# create
def post_create(request):
  if request.method == "GET":
    return render(request, 'postCreate.html')
  if request.method == "POST":
    posts = PostModel.objects.create(
    title = request.POST.get('title'),
    body = request.POST.get('body'),
    created_at = request.POST.get('created')
    )
    posts.save()
    messages.success(request, "The post has been created successfully.")
    return redirect('/blog/')

#post Detail
def post_detail(request, post_id):
    posts = PostModel.objects.get(id=post_id)
    return render(request, 'postDetail.html', {"posts":posts})

#post Update
def post_update(request, post_id):
    post = get_object_or_404(PostModel, id=post_id)
    if request.method == "GET":
        post.created_at = post.created_at.strftime('%Y-%m-%dT%H:%M')
        return render(request, 'postUpdate.html', {"post": post})
    elif request.method == "POST":
        post.title = request.POST.get('title')
        post.body = request.POST.get('body')
        created_at_str = request.POST.get('created')
        if created_at_str:
            post.created_at = datetime.datetime.strptime(created_at_str, '%Y-%m-%dT%H:%M')
        post.save()
        messages.success(request, "The post has been updated successfully.")
        return redirect('/blog/')

#post delete
def post_delete(request, post_id):
    posts = PostModel.objects.filter(id = post_id)
    posts.delete()
    messages.success(request, "The post has been deleted successfully.")
    return redirect('/blog/')

#log in
from django.contrib.auth import authenticate, login, logout

def login_view(request):
  if request.method == "GET":
    return render(request, 'login.html')
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username = username, password = password)
    if user is not None:
      login(request, user)
      messages.success(request, "you are now logged in as "+ username)
      return redirect('/blog/')
    else:
      messages.error(request, "username or password is incorrect!")
      return render(request, 'login.html')

#log out
def logout_view(request):
  logout(request)
  return redirect('/login/')