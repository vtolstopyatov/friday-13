from rest_framework import viewsets
from vacancies.models import Language

from .serializers import LanguageSerializer


class LanguageViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Вьюсет разговорных языков.
    """

    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
