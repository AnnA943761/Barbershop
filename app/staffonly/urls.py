from django.urls import path, include
from .views import register, posts, create_post

app_name = "staffonly"

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/',register, name="register"),
        path("blog/", posts, name = "blog"),
    path("new_post/", create_post, name = "create_post"),
]
