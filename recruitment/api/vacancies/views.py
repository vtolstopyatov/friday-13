from rest_framework import viewsets, status
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from vacancies.models import Cv, Vacancy, Applicant, VacancyResponse
from .serializers import (CvCreateSerializer, CvSerializer,
                          VacancySerializer, InviteApplicantSerializer, VacancyResponseSerializer)
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
        serializer = VacancyResponseSerializer(data=request.data)
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


class ResponsesViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        if self.action in ('list', 'retrieve', 'destroy'):
            return Applicant.objects.filter(vacancy_responses__vacancy__id=self.kwargs['vacancy_pk'])
        return VacancyResponse.objects.filter(vacancy__id=self.kwargs['vacancy_pk'])

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve', 'destroy'):
            return ApplicantSerializer
        return InviteApplicantSerializer

    def create(self, request, *args, **kwargs):
        '''Добавляет соискателя к вакансии.'''
        request.data['vacancy'] = self.kwargs['vacancy_pk']
        request.data['status'] = VacancyResponse.STATUS[1][0]
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    def destroy(self, request, *args, **kwargs):
        '''Удаляет соискателя из вакансии.'''
        obj = VacancyResponse.objects.filter(
            vacancy__id=self.kwargs['vacancy_pk'],
            applicant__id=self.kwargs['pk'],
        )
        if obj.exists():
            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {'errors': 'not in added'},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def partial_update(self, request, *args, **kwargs):
        '''Обновляет статус отклика на вакансию.'''
        request.data['vacancy'] = self.kwargs['vacancy_pk']
        request.data['applicant'] = self.kwargs['pk']
        # obj = Objects
        serializer = self.get_serializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )
