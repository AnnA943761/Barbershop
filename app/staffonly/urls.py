from django.urls import path, include
from .views import create_post, detail_post, edit_post, delete_post, profile_reviews, RegisterUser, ProfileView, ListPost

app_name = "staffonly"

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', RegisterUser.as_view(), name='register'),
    path("", ProfileView.as_view(), name="profile"),
    path("create_post/", create_post, name="create_post"),
    path("list_posts/", ListPost.as_view(), name="list_posts"),
    path("list_posts/<int:post_id>/", detail_post, name="detail_post"),
    path("edit_post/<int:post_id>/", edit_post, name="edit_post"),
    path("list_posts/<int:post_id>/delete/", delete_post, name="delete_post"),
    path("profile_reviews/", profile_reviews, name="profile_reviews")
]