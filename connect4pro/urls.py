from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Connect4Pro",
        default_version="v1",
        description="Исправленная версия коннекта",
        terms_of_service="",
        contact=openapi.Contact(email="makarovdmitry089@gmail.com"),
        license=openapi.License(name="No License"),
    ),
    # patterns=[
    #     path("api/", include("myapi.urls")),
    # ],
    public=True,
    permission_classes=(
        [
            permissions.AllowAny,
        ]
    ),
)
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("", include("social_django.urls", namespace="social")),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("", include("apps.posts.urls")),
    path("", include("apps.users.urls")),
    path("", include("apps.adverts.urls")),
]
