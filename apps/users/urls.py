from django.urls import path

from apps.users.views import auth, UserListView

urlpatterns = [
    path("auth/", auth),
    path("users/list", UserListView.as_view(), name="user-list"),
]