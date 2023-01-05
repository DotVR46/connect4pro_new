from django.db.models import Prefetch
from django_filters import rest_framework as filters
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics

from apps.users.models import Profile
from apps.users.serializers import UserSerializer


class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all().prefetch_related(
        Prefetch(
            "user_profile",
            queryset=Profile.objects.all()
            .select_related("user")
            .only("avatar", "profile_type", "premium"),
        )
    )
    filter_backends = (filters.DjangoFilterBackend,)


def auth(request):
    return render(request, "oauth.html")
