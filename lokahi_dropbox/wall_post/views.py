from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render
from wall_post.forms import *
from django.contrib.auth.models import User
from frontend.models import *
from django.http import HttpResponseRedirect


@csrf_protect
def wall(request):
    return render(request, 'wall_post/wall_post.html')


@csrf_protect
def post(request):
    return render(request, 'wall_post/post.html', {'form': PostForm(request)})


@csrf_protect
def view_wall(request):
    posts = Post.objects.all()
    return render(request, 'wall_post/view_wall.html', {'posts': posts})


@csrf_protect
def make_post(request):
    if request.method == "POST":
        form = PostForm(data=request.POST)
        if form.is_valid():
            username = request.user.username
            message = form.cleaned_data['message']
            if form.cleaned_data['anonymous']:
                post = Post.objects.create(message=message, sender="anonymous")
            else:
                post = Post.objects.create(message=message, sender=username)
            return HttpResponseRedirect('/wall/',)
