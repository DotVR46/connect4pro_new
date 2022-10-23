from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.posts.models import Post
from apps.posts.serializers import PostSerializer


class PostApiTestCase(APITestCase):
    def test_get_list(self):
        post_1 = Post.objects.create(title="Post1", content="Test post1")
        post_2 = Post.objects.create(title="Post2", content="Test post2")
        url = reverse("posts-list")
        response = self.client.get(url)
        serializer_data = PostSerializer([post_1, post_2], many=True).data

        self.assertEqual(serializer_data, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_get_detail(self):
        post = Post.objects.create(title="Post", content="Test post")
        url = reverse("post-detail", kwargs={"slug": post.slug})
        response = self.client.get(url)
        serializer_data = PostSerializer(post).data

        self.assertEqual(serializer_data, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
