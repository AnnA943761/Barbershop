from django.urls import path

from .views import home, list_reviews, create_reviews

app_name = "blog"

urlpatterns = [
    path("", home, name="home"),
    path("reviews/", list_reviews, name = "list_reviews"),
    path("create_review", create_reviews, name="create_review"),
]