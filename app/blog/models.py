
from django.db import models
from staffonly.models import Master

class Review(models.Model):
    name = models.CharField(max_length=20, verbose_name="Имя", blank=False)
    phone = models.CharField(max_length=10, verbose_name="Номер телефона", blank=False)
    content = models.TextField(max_length=100, verbose_name="Отзыв", blank=False)
    publish = models.BooleanField(verbose_name="Состояние", default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    grade = models.IntegerField(verbose_name="Оценка", default=5, blank=False)
    master = models.ForeignKey(Master, verbose_name="Мастер", on_delete=models.DO_NOTHING)


    def __str__(self) -> str:
        return f"{self.grade}"