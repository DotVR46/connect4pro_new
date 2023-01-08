from django.urls import path

from apps.users.views import auth, UserListView, UserDetailView

urlpatterns = [
    path("auth/", auth),
    path("users/list", UserListView.as_view(), name="user-list"),
    path("users/id-<int:id>", UserDetailView.as_view(), name="user-detail"),
]