from django.urls import path, include
from .views import register, profile, create_post, list_posts, detail_post, edit_post, delete_post

app_name = "staffonly"

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path("", profile, name="profile"),
    path("create_post/", create_post, name="create_post"),
    path("list_posts/", list_posts, name="list_posts"),
    path("list_posts/<int:post_id>/", detail_post, name="detail_post"),
    path("edit_post/<int:post_id>/", edit_post, name="edit_post"),
    path("list_posts/<int:post_id>/delete/", delete_post, name="delete_post"),
]
