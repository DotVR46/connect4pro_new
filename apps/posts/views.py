from django_filters import rest_framework as filters
from rest_framework import generics

from apps.posts.models import Post
from apps.posts.serializers import PostSerializer


class PostListView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ["post_type"]


class PostDetailView(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = "slug"
