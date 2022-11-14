from django.contrib.auth.models import User
from rest_framework import serializers

from apps.users.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("avatar", "profile_type", "premium")


class UserSerializer(serializers.ModelSerializer):
    user_profile = ProfileSerializer()

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "is_active",
            "date_joined",
            "user_profile",
        )
