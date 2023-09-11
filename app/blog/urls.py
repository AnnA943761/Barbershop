from django.urls import path

from .views import home, ListReviews, ListPosts, CreateReview

app_name = "blog"

urlpatterns = [
    path("", home, name="home"),
    path("blog/", ListPosts.as_view(), name="blog"),
    path("reviews/", ListReviews.as_view(), name="list_reviews"),
    path("create_review/", CreateReview.as_view(), name="create_review")
]