from rest_framework import serializers

from apps.adverts.models import Advert
from apps.users.serializers import UserSerializer


class AdvertSerializer(serializers.ModelSerializer):
    # user = UserSerializer()

    class Meta:
        model = Advert
        fields = ("user", "user_email", "title", "content", "created", "price", "currency")
        read_only_fields = ("user",)
