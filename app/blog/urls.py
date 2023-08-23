from django.urls import path

from .views import home, list_reviews, posts, create_post, create_reviews

app_name = "blog"

urlpatterns = [
    path("", home, name="home"),
      path("reviews/", list_reviews, name = "list_reviews"),
    path("blog/", posts, name = "blog"),
    path("new_post/", create_post, name = "create_post"),
    path("create_review", create_reviews, name="create_review"),
]