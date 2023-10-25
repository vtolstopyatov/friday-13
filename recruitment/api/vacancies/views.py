from rest_framework import viewsets

from vacancies.models import Cv, Vacancy
from .serializers import (CvCreateSerializer, CvSerializer,
                          VacancySerializer,)


class CvViewSet(viewsets.ModelViewSet):

    queryset = Cv.objects.all()
    serializer_class = CvSerializer

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return CvSerializer
        return CvCreateSerializer


class VacancyViewSet(viewsets.ModelViewSet):

    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

    # def get_serializer_class(self):
    #     if self.action in ('list', 'retrieve'):
    #         return VacancySerializer
    #     return VacancyCreateSerializer
