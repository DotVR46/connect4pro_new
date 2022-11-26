# Generated by Django 4.1.1 on 2022-11-26 20:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Advert",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=300, verbose_name="Заголовок")),
                ("content", models.TextField(verbose_name="Содержание")),
                (
                    "price",
                    models.IntegerField(
                        blank=True, default=0, max_length=8, verbose_name="Цена"
                    ),
                ),
                (
                    "currency",
                    models.CharField(
                        choices=[("usd", "US Dollar"), ("kgs", "KG Сом")],
                        default="usd",
                        max_length=3,
                        verbose_name="Валюта",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now=True, verbose_name="Дата создания"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Объявление",
                "verbose_name_plural": "Объявления",
                "ordering": ("-created",),
            },
        ),
    ]
