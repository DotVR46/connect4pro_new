from rest_framework import generics
from apps.posts.models import Post
from apps.posts.serializers import PostSerializer


class PostListView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        post_type = self.kwargs["type"]
        return Post.objects.filter(post_type=post_type)


class PostDetailView(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
