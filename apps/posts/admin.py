from django.contrib import admin

from apps.posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "post_type", "date", "published")
    list_filter = ("published", "post_type")
    list_editable = ("published",)
