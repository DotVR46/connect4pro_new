from django.urls import path

from apps.posts.views import PostListView, PostDetailView

urlpatterns = [
    path("api/posts", PostListView.as_view(), name="posts-list"),
    path("api/post/<str:slug>", PostDetailView.as_view(), name="post-detail"),
]