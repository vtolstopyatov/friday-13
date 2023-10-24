from rest_framework import serializers
from vacancies.models import City


class CitySerializer(serializers.ModelSerializer):
    '''Сериализатор городов.'''

    class Meta:
        model = City
        fields = ('id', 'name', 'region', 'country')
