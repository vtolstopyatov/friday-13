from rest_framework import serializers
from vacancies.models import Language


class LanguageSerializer(serializers.ModelSerializer):
    '''Сериализатор языков.'''

    class Meta:
        model = Language
        fields = ('id', 'language')
