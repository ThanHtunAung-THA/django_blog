from django.shortcuts import render, redirect
from blog.models import PostModel

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
    return redirect('/blog/')