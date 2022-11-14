from django_filters import rest_framework as filters
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics

from apps.users.serializers import UserSerializer


class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)


def auth(request):
    return render(request, "oauth.html")
