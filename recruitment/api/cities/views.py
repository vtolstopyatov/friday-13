from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from vacancies.models import City

from .filters import CityFilter
from .serializers import CitySerializer


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Viewset города.
    """

    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CityFilter