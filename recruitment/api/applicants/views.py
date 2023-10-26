from rest_framework import viewsets

from vacancies.models import Applicant
from .serializers import ApplicantSerializer


class ApplicantViewSet(viewsets.ReadOnlyModelViewSet):
    'Viewset соискателей.'
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer
