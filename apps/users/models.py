from django.contrib.auth.models import User
from django.db import models

PROFILE_TYPE = (("business", "Бизнес"), ("provider", "Провайдер"))


class Profile(models.Model):
    user = models.OneToOneField(
        User, primary_key=True, verbose_name="Пользователь", on_delete=models.CASCADE, related_name="user_profile"
    )
    avatar = models.ImageField(
        default="default.jpg", upload_to="profile_images/", verbose_name="Аватар"
    )
    profile_type = models.CharField(
        choices=PROFILE_TYPE,
        verbose_name="Тип профиля",
        max_length=8,
        default="business",
    )
    premium = models.BooleanField(default=False, verbose_name="Премиум-статус")

    def __str__(self):
        return f"{self.user.email} - {self.profile_type} - Премиум: {self.premium}"

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
