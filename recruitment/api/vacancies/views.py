from rest_framework import viewsets, status
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from vacancies.models import Cv, Vacancy, Applicant, VacancyResponse
from .serializers import (CvCreateSerializer, CvSerializer,
                          VacancySerializer, InviteApplicantSerializer)
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

    @applicants.mapping.post
    def applicants_add(self, request, pk=None):
        '''Добавляет соискателя к вакансии.'''
        vacancy = self.get_object()
        request.data['vacancy'] = pk
        serializer = InviteApplicantSerializer(data=request.data)
        if serializer.is_valid():
            applicant = serializer.validated_data.get('applicant')
            obj, created = VacancyResponse.objects.get_or_create(
                applicant=applicant,
                vacancy=vacancy,
                defaults={'status': VacancyResponse.STATUS[1][0]},
            )
            if created:
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED,
                )
            return Response(
                {'errors': 'already added'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    @applicants.mapping.delete
    def applicants_remove(self, request, pk=None):
        '''Удаляет соискателя из вакансии.'''
        vacancy = self.get_object()
        request.data['vacancy'] = pk
        serializer = InviteApplicantSerializer(data=request.data)
        if serializer.is_valid():
            applicant = serializer.validated_data.get('applicant')
            invite = VacancyResponse.objects.filter(
                applicant=applicant,
                vacancy=vacancy,
            )
            if invite.exists():
                invite.delete()
                return Response(
                    serializer.data,
                    status=status.HTTP_204_NO_CONTENT,
                )
            return Response(
                {'errors': 'not in added'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    @applicants.mapping.patch
    def applicants_change_status(self, requset, pk=None):
        pass