from django.contrib import admin

from apps.adverts.models import Advert


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "price", "currency", "created")
