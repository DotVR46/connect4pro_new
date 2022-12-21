from django.contrib.auth.models import User
from django.db import models


CURRENCY = (("usd", "US Dollar"), ("kgs", "KG Сом"))


class Advert(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="author",
    )
    title = models.CharField(max_length=300, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    price = models.IntegerField(verbose_name="Цена", default=0, blank=True)
    currency = models.CharField(
        verbose_name="Валюта", choices=CURRENCY, default="usd", max_length=3
    )
    created = models.DateTimeField(verbose_name="Дата создания", auto_now=True)

    @property
    def user_email(self):
        return self.user.email

    def __str__(self):
        return f"{self.title} - {self.user.email}"

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        # ordering = ("-created",)
