from datetime import datetime
from django.db import models

TYPE = (("grant", "Грант"), ("invest", "Инвестиция"))


class GrantInvest(models.Model):
    title = models.CharField(max_length=500, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    location = models.CharField(
        max_length=200, verbose_name="Место проведения", default="online", blank=True
    )
    type = models.CharField(
        max_length=20, verbose_name="Тип записи", choices=TYPE, default="grant"
    )
    date = models.DateTimeField(verbose_name="Дата проведения", default=datetime.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Гранты и инвестиции"
        verbose_name_plural = "Гранты и инвестиции"
