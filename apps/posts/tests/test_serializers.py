from django.test import TestCase
from apps.posts.models import Post
from apps.posts.serializers import PostSerializer


class PostSerializerTestCase(TestCase):
    def test_ok(self):
        post_1 = Post.objects.create(title="Post 1", content="Post 1")
        post_2 = Post.objects.create(title="Post 2", content="Post 2")
        data = PostSerializer([post_1, post_2], many=True).data

        expected_data = [
            {
                "id": post_1.id,
                "title": "Post 1",
                "slug": "post_post-1",
                "intro": "",
                "content": "Post 1",
                "post_type": "post",
                "date": post_1.date.isoformat(),
                "published": True,
            },
            {
                "id": post_2.id,
                "title": "Post 2",
                "slug": "post_post-2",
                "intro": "",
                "content": "Post 2",
                "post_type": "post",
                "date": post_2.date.isoformat(),
                "published": True,
            },
        ]

        self.assertEqual(expected_data, data)
