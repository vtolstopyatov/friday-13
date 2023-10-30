from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from vacancies.models import Applicant
from .serializers import ApplicantSerializer
from .filters import ApplicantFilter


class ApplicantViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Viewset соискателей.
    """

    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ApplicantFilter
