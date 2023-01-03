from django.contrib import admin

from apps.grants_invests.models import GrantInvest


@admin.register(GrantInvest)
class GrantInvestAdmin(admin.ModelAdmin):
    list_display = ("title", "date")
