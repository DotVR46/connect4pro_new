# Generated by Django 4.1.1 on 2022-10-18 16:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GrantInvest",
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
                ("title", models.CharField(max_length=500, verbose_name="Название")),
                ("description", models.TextField(verbose_name="Описание")),
                (
                    "location",
                    models.CharField(blank=True, default="online", max_length=200),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[("grant", "Грант"), ("invest", "Инвестиция")],
                        default="grant",
                        max_length=20,
                        verbose_name="Тип записи",
                    ),
                ),
                (
                    "date",
                    models.DateTimeField(
                        default=datetime.datetime.now, verbose_name="Дата проведения"
                    ),
                ),
            ],
            options={
                "verbose_name": "Гранты и инвестиции",
                "verbose_name_plural": "Гранты и инвестиции",
            },
        ),
    ]
