from rest_framework import viewsets
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend

from vacancies.models import Cv, Vacancy, Applicant
from .serializers import (CvCreateSerializer, CvSerializer,
                          VacancySerializer,)
from .filters import CvFilter, VacancyFilter
from ..applicants.serializers import ApplicantSerializer

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

    @action(detail=True, methods=['get'])
    def applicants(self, request, pk=None):
        pages = self.paginate_queryset(
            Applicant.objects.filter(vacancy_responses__vacancy=pk).order_by('pk')
        )
        serializer = ApplicantSerializer(
            pages, many=True, context={'request': request},
        )
        return self.get_paginated_response(serializer.data)

    # def get_serializer_class(self):
    #     if self.action in ('list', 'retrieve'):
    #         return VacancySerializer
    #     return VacancyCreateSerializer
