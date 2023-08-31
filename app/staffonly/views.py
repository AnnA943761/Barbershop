from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

# Create your views here.


def register(request):
    if register.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('staffonly/:home')
    context = {"form": form}
    return render(request, 'registration/register.html', context=context)
COUNT = 0

@login_required
def profile(request):
    return render(request, "staffonly/profile.html")

@login_required
def list_posts(request):
    posts = Post.objects.filter(publish=False)
    context = {"posts": posts}
    print(context)
    return render(request, "staffonly/list_posts.html", context=context)

@login_required
def detail_post(request, post_id):
    detail_post = Post.objects.get(id=post_id)
    context = {"detail_post":detail_post}
    return render(request, "staffonly/detail_post.html", context=context)

@login_required
def create_post(request):
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/staffonly')
    context = {"form": form}
    return render(request, "staffonly/create_post.html", context=context)

@login_required
def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method != 'POST':
        form = PostForm(instance=post)
    else:
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/staffonly/list_posts/')
    context = {"form": form, "post": post}
    return render(request, "staffonly/edit_post.html", context=context)

@login_required
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        post.delete()
        return redirect('/staffonly/list_posts/')
    return render(request, 'staffonly/delete_post.html', context={"post": post})


