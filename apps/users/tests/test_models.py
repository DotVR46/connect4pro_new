from django.contrib.auth.models import User
from django.test import TestCase

from apps.users.models import Profile


class ProfileModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            "user", email="test@test.com", password="123456"
        )
        self.profile = Profile.objects.create(user=self.user)

    def test_one_to_one(self):
        self.assertEqual(self.user, self.profile.user)

    def test_dunder_str(self):
        string = f"{self.user.email} - {self.profile.profile_type} - Премиум: {self.profile.premium}"
        self.assertEqual(string, self.profile.__str__())

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))
        self.assertTrue(isinstance(self.profile.user, User))
