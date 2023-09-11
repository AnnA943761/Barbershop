from django.shortcuts import render, redirect
from django.urls import reverse
from django.urls import reverse_lazy
from .models import Review
from .forms import ReviewForm
from django.views.generic import ListView, TemplateView, CreateView

from staffonly.models import Post

# Create your views here.

def home(request):
    return render(request, "blog/home.html")
    
"""def list_reviews(request):
    reviews = Review.objects.filter(publish=True)
    context = {"reviews": reviews}
    return render(request, "blog/reviews.html", context=context)
"""
class ListReviews(ListView):
    queryset = Review.objects.filter(publish=True)
    context_object_name = "reviews"
    template_name = "blog/reviews.html"


"""def create_review(request):
    if request.method != 'POST':
        form = ReviewForm()
    else:
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/reviews')
    context = {"form": form}
    return render(request, "blog/create_review.html", context=context)"""

class CreateReview(CreateView):
    model = Review
    fields = ["name", "phone", "content", "grade", "master"]
    template_name = "blog/create_review.html"
    success_url = reverse_lazy("blog:blog")

"""
def list_posts(request):
    posts = Post.objects.filter(publish=True)
    context = {"posts": posts}
    return render(request, "blog/blog.html", context=context)
"""
class ListPosts(ListView):
    queryset = Post.objects.filter(publish=True)
    context_object_name = "posts"
    template_name = "blog/blog.html"