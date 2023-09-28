from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import AdvertViewSet

router = DefaultRouter()

urlpatterns = [
    path("advert-list/", AdvertViewSet.as_view({"get": "list"}), name="advert-list"),
    path(
        "advert/<int:pk>/",
        AdvertViewSet.as_view({"get": "retrieve"}),
        name="advert-detail",
    ),
]

urlpatterns += router.urls
