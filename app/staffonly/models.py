from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=200, blank=False)
    content = models.TextField(verbose_name="Контент", blank=False)
    publish = models.BooleanField(verbose_name="Состояние", default=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title