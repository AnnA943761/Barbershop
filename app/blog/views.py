from django.shortcuts import render, redirect
from .models import Post, Review
from .forms import PostForm, ReviewForm

# Create your views here.

def home(request):
    print(request)
    return render(request, "blog/home.html")

def list_reviews(request):
    reviews = Review.object.filter(publish=True)
    context=("review")

def posts(request):
    # Запрос в базу данных и запись данных в переменную posts
    posts = Post.objects.filter(publish=True)
    #print(posts)
    context = {"posts": posts}
    return render(request,  "blog/blog.html", context=context)

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

def create_reviews(request):
    if request.method != 'POST':
        form = ReviewForm()
    else:
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/reviews')
    context = {"form": form}
    return render(request, "blog/create_reviews", context=context)