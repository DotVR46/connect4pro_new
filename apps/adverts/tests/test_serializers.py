from django.contrib.auth.models import User
from django.test import TestCase

from apps.adverts.models import Advert
from apps.adverts.serializers import AdvertSerializer


class AdvertSerializerTestCase(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username="user", password="123456")
        self.advert_1 = Advert.objects.create(
            title="test", user=self.user, content="test"
        )
        self.advert_2 = Advert.objects.create(
            title="test_2", user=self.user, content="test_2"
        )

    def test_serializer(self):
        data = AdvertSerializer([self.advert_1, self.advert_2], many=True).data
        expected_data = [
            {
                "user": self.user.id,
                "user_email": "",
                "title": "test",
                "content": "test",
                "created": self.advert_1.created.isoformat(),
                "price": 0,
                "currency": "usd",
            },
            {
                "user": self.user.id,
                "user_email": "",
                "title": "test_2",
                "content": "test_2",
                "created": self.advert_2.created.isoformat(),
                "price": 0,
                "currency": "usd",
            },
        ]
        self.assertEqual(data, expected_data)