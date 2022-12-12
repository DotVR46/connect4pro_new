from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.adverts.models import Advert
from apps.adverts.permissions import IsOwnerOrReadOnly
from apps.adverts.serializers import AdvertSerializer


class AdvertListView(generics.ListAPIView):
    serializer_class = AdvertSerializer
    queryset = Advert.objects.all()


class AdvertUpdateView(generics.UpdateAPIView):
    serializer_class = AdvertSerializer
    queryset = Advert.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    lookup_field = "id"


class AdvertCreateView(generics.CreateAPIView):
    serializer_class = AdvertSerializer
    queryset = Advert.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AdvertRetrieveView(generics.RetrieveAPIView):
    serializer_class = AdvertSerializer
    queryset = Advert.objects.all()
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"
