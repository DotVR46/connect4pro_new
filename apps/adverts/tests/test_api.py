from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from apps.adverts.models import Advert
from apps.adverts.serializers import AdvertSerializer


class AdvertApiTestCase(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username="test", password="123456")
        self.advert_1 = Advert.objects.create(
            title="test1", content="test1", user=self.user
        )
        self.advert_2 = Advert.objects.create(
            title="test2", content="test2", user=self.user
        )

    def test_get_list(self):
        url = reverse("advert-list")
        response = self.client.get(url)
        serializer_data = AdvertSerializer(
            [self.advert_1, self.advert_2], many=True
        ).data

        self.assertEqual(serializer_data, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def def_get_detail(self):
        url = reverse("advert-get", kwargs={"id": 1})
        response = self.client.get(url)
        serializer_data = AdvertSerializer(self.advert_1).data

        self.assertEqual(serializer_data, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_update(self):
        pass

    def test_create(self):
        pass
