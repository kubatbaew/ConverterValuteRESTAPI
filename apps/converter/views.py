from rest_framework import viewsets, mixins

from apps.converter.models import Converter
from apps.converter.serializers import ConverterSerializer


class ConverterAPIViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Converter.objects.all()
    serializer_class = ConverterSerializer
    lookup_field = 'id'
