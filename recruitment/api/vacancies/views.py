from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from vacancies.models import Cv, Vacancy
from .serializers import (CvCreateSerializer, CvSerializer,
                          VacancySerializer,)
from .filters import CvFilter, VacancyFilter


class CvViewSet(viewsets.ModelViewSet):

    queryset = Cv.objects.all()
    serializer_class = CvSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = CvFilter

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return CvSerializer
        return CvCreateSerializer


class VacancyViewSet(viewsets.ModelViewSet):

    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = VacancyFilter

    # def get_serializer_class(self):
    #     if self.action in ('list', 'retrieve'):
    #         return VacancySerializer
    #     return VacancyCreateSerializer
