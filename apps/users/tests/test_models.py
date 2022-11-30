from django.contrib.auth.models import User
from django.test import TestCase

from apps.users.models import Profile


class ProfileModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            "user", email="test@test.com", password="123456"
        )

    def test_one_to_one(self):
        self.assertEqual(self.user, self.user.user_profile.user)

    def test_dunder_str(self):
        string = f"{self.user.email} - {self.user.user_profile.profile_type} - Премиум: {self.user.user_profile.premium}"
        self.assertEqual(string, self.user.user_profile.__str__())

    def test_instance(self):
        self.assertTrue(isinstance(self.user.user_profile, Profile))
        self.assertTrue(isinstance(self.user.user_profile.user, User))
