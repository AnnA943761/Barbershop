from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
    if register.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:home')
    context = {"form": form}
    return render(request, 'registration/register.html', context=context)

@login_required
def pofile(request):
    pass

@login_required
def posts(request):
    # Запрос в базу данных и запись данных в переменную posts
    posts = Post.objects.filter(publish=True)
    #print(posts)
    context = {"posts": posts}
    return render(request,  "blog/blog.html", context=context)

@login_required
def create_post(request):
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/blog')
    context = {"form": form}
    return render(request, "blog/create_post.html", context=context)

