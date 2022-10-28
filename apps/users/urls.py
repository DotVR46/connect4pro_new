from django.urls import path

from apps.users.views import auth

urlpatterns = [
    path("auth/", auth)
]