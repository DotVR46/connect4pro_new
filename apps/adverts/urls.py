from django.urls import path

from apps.adverts.views import AdvertListView, AdvertUpdateView, AdvertCreateView, AdvertRetrieveView

urlpatterns = [
    path("adverts/list", AdvertListView.as_view(), name="advert-list"),
    path("adverts/update/<int:id>", AdvertUpdateView.as_view(), name="advert-update"),
    path("adverts/create", AdvertCreateView.as_view(), name="advert-create"),
    path("adverts/<int:id>", AdvertRetrieveView.as_view(), name="advert-get"),
]
