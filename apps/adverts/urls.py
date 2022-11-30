from django.urls import path

from apps.adverts.views import AdvertListView, AdvertUpdateView

urlpatterns = [
    path("adverts/list", AdvertListView.as_view(), name="advert-list"),
    path("adverts/update/<int:id>", AdvertUpdateView.as_view(), name="advert-update"),
]
