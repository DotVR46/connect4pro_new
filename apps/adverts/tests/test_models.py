from django.contrib.auth.models import User
from django.test import TestCase

from apps.adverts.models import Advert


class AdvertModelTestCase(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            username="test", password="test", email="test@test.com"
        )
        self.advert = Advert.objects.create(
            title="Test", user=self.user, content="Test"
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.advert, Advert))

    def test_dunder_str(self):
        string = f"{self.advert.title} - {self.advert.user.email}"
        self.assertEqual(string, self.advert.__str__())

    def test_user_email(self):
        self.assertEqual(self.user.email, self.advert.user_email)
