from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, TemplateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import Master

from .models import Post
from .forms import PostForm


class RegisterUser(CreateView):
    model = User
    fields = '__all__'
    template_name = "registration/register.html"
    success_url = reverse_lazy("blog:home")
"""
def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:home')
    context = {"form": form}
    return render(request, 'registration/register.html', context=context)
"""

class ProfileView(TemplateView):
    template_name = "staffonly/profile.html"
"""    
@login_required
def profile(request):
    return render(request, "staffonly/profile.html")"""

class ListPost(ListView):
    queryset = Post.objects.filter(publish=True)
    context_object_name = "posts"
    template_name = "staffonly/list_posts.html"

"""@login_required
def list_posts(request):
    posts = Post.objects.filter(publish=False)
    context = {"posts": posts}
    return render(request, "staffonly/list_posts.html", context=context)"""

@login_required
def detail_post(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {"post": post}
    return render(request, 'staffonly/detail_post.html', context=context)



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

def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('/staffonly/list_posts/')
    return render(request, 'staffonly/delete_post.html', context={"post": post})

def profile_reviews(request):
    if request.user.is_authenticated:
        print(request.user.username)
    return render(request, "staffonly/profile_reviews.html")


