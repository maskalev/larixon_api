from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Advert
from .serializers import AdvertSerializer


class AdvertViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Advert.objects.prefetch_related("city", "category").order_by("-created")
    serializer_class = AdvertSerializer

    def retrieve(self, request, pk=None):
        queryset = self.queryset
        advert = get_object_or_404(queryset, pk=pk)
        advert.views += 1
        advert.save()
        serializer = self.serializer_class(advert)
        return Response(serializer.data)
