from django.db import models
from django.template.defaultfilters import slugify
from unidecode import unidecode

POST_TYPES = (("blog", "Блог"), ("post", "Новость"), ("event", "Событие"))


class Post(models.Model):
    title = models.CharField(max_length=300, verbose_name="Название", db_index=True)
    slug = models.CharField(max_length=300, verbose_name="Слаг", blank=True)
    intro = models.CharField(max_length=600, verbose_name="Описание", blank=True)
    content = models.TextField(verbose_name="Содержание")
    post_type = models.CharField(
        verbose_name="Тип записи", choices=POST_TYPES, default="post", max_length=5
    )
    date = models.DateTimeField(auto_now=True, verbose_name="Дата публикации")
    published = models.BooleanField(verbose_name="Статус публикации", default=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.post_type + "_" + self.title))
        super(Post, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
