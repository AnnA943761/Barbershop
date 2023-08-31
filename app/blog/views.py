from django.shortcuts import render, redirect
from .models import Review
from blog.forms import ReviewForm

# Create your views here.

def home(request):
    print(request)
    return render(request, "blog/home.html")

def list_reviews(request):
    reviews = Review.object.filter(publish=True)
    context=("review")

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