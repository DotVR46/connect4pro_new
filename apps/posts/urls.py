from django.urls import path

from apps.posts.views import PostListView, PostDetailView

urlpatterns = [
    path("posts/list", PostListView.as_view(), name="posts-list"),
    path("posts/<str:slug>", PostDetailView.as_view(), name="post-detail"),
]