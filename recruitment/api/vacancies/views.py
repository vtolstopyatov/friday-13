from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from vacancies.models import Applicant, Vacancy, VacancyResponse

from vacancies.models import Vacancy, Applicant, VacancyResponse
from .filters import VacancyFilter
from ..applicants.serializers import VacancyApplicantSerializer
from ..applicants.filters import ApplicantFilter
from .filters import VacancyFilter
from .serializers import (SendMailSerializer, VacancyResponseSerializer,
                          VacancySerializer)


class VacancyViewSet(viewsets.ModelViewSet):
    """
    Viewset вакансий.
    """

    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = VacancyFilter


class ResponsesViewSet(viewsets.ModelViewSet):
    """
    Viewset кандидатов по вакансиям.
    """

    filter_backends = (DjangoFilterBackend,)
    filterset_class = ApplicantFilter

    def get_queryset(self):
        if self.action in ('list', 'retrieve', 'destroy'):
            return Applicant.objects.filter(vacancy_responses__vacancy__id=self.kwargs['vacancy_pk'])
        return VacancyResponse.objects.filter(vacancy__id=self.kwargs['vacancy_pk'])

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve', 'destroy'):
            return VacancyApplicantSerializer
        return VacancyResponseSerializer

    def create(self, request, *args, **kwargs):
        """
        Добавляет соискателя к вакансии.
        """
        request.data['vacancy'] = self.kwargs['vacancy_pk']
        request.data['status'] = VacancyResponse.STATUS[1][1]
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
        """
        Удаляет соискателя из вакансии.
        """
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

    def partial_update(self, request, vacancy_pk=None, pk=None, *args, **kwargs):
        """
        Обновляет статус отклика на вакансию.
        """
        request.data['vacancy'] = vacancy_pk
        request.data['applicant'] = pk
        obj = get_object_or_404(
            VacancyResponse,
            vacancy__id=vacancy_pk,
            applicant__pk=pk,
        )
        serializer = self.get_serializer(obj, data=request.data, partial=True)
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

    @action(detail=True, methods=['post'])
    def send_mail(self, request, pk=None):
        '''Отправляет письмо соискателю.'''
        serializer = SendMailSerializer(context={'request': request})
        subject = serializer.validated_data['subject']
        body = serializer.validated_data['body']
        send_mail(
            subject,
            body,
            None,
            [serializer.validated_data['email']],
            fail_silently=True,
        )
        return Response(status=status.HTTP_200_OK)
