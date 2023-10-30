from rest_framework import serializers
from vacancies.models import City


class CitySerializer(serializers.ModelSerializer):
    """
    Сериалайзер города.
    """

    class Meta:
        model = City
        fields = ("id", "name", "region", "country")
