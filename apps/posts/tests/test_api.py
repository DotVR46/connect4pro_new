from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.posts.models import Post
from apps.posts.serializers import PostSerializer


class PostApiTestCase(APITestCase):
    def setUp(self) -> None:
        self.post_1 = Post.objects.create(
            title="Post1", content="Test post1", post_type="post"
        )
        self.post_2 = Post.objects.create(
            title="Post2", content="Test post2", post_type="blog"
        )

    def test_get_list(self):
        url = reverse("posts-list")
        response = self.client.get(url)
        serializer_data = PostSerializer([self.post_1, self.post_2], many=True).data

        self.assertEqual(serializer_data, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_get_detail(self):
        url = reverse("post-detail", kwargs={"slug": self.post_1.slug})
        response = self.client.get(url)
        serializer_data = PostSerializer(self.post_1).data

        self.assertEqual(serializer_data, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_filter(self):
        url = reverse("posts-list")
        response = self.client.get(url, data={"post_type": "blog"})
        serializer_data = PostSerializer([self.post_1, self.post_2], many=True).data

        self.assertEqual(serializer_data, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
