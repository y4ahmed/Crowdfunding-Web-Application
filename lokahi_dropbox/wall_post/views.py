from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from wall_post.models import Post
from wall_post.forms import PostForm
from frontend.models import BaseUser
from django.http import HttpResponseRedirect
# from django.contrib.auth.models import User


@csrf_protect
def wall(request):
    base = BaseUser.objects.get(user=request.user)
    return render(
        request,
        'wall_post/wall_post.html',
        {'type': base.user_role, }
    )


@csrf_protect
def post(request):
    base = BaseUser.objects.get(user=request.user)
    return render(
        request,
        'wall_post/post.html',
        {'form': PostForm(request), 'type': base.user_role}
    )


@csrf_protect
def view_wall(request):
    base = BaseUser.objects.get(user=request.user)
    posts = Post.objects.all()
    return render(
        request,
        'wall_post/view_wall.html',
        {'posts': posts, 'type': base.user_role}
    )


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
