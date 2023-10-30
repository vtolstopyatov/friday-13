from re import match
from rest_framework import serializers

from rest_framework.serializers import ValidationError

from vacancies.models import Cv, Vacancy, LanguageLevel, Expirience, Applicant, VacancyResponse, Language
from django.contrib.auth import get_user_model

User = get_user_model()


class DisplayChoiceField(serializers.ChoiceField):
    def to_representation(self, obj):
        if obj == '' and self.allow_blank:
            return obj
        return self._choices[obj]

    def to_internal_value(self, data):
        if data == '' and self.allow_blank:
            return ''

        for key, val in self._choices.items():
            if val == data:
                return key
        self.fail('invalid_choice', input=data)


class LanguageLevelSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(
        queryset=Language.objects.all(),
        source='language.pk',
    )
    language = serializers.ReadOnlyField(source='language.language')

    class Meta:
        model = LanguageLevel
        fields = ['id', 'language', 'level']


class CvCreateSerializer(serializers.ModelSerializer):
    """Кастомный сериализатор для создания резюме."""

    class Meta:
        model = Cv
        fields = (
            "title",
            "optional_description",
            "city",
            "salary",
            "experience",
            "currency",
        )

    def validate_name_cv(self, value):
        if match(r'^[-+]?[0-9]+$', value):
            raise ValidationError("Некорректное название резюме.")
        return value

    def create(self, validated_data):
        author = self.context.get('request').user
        cv = Cv.objects.create(author=author, **validated_data)
        return cv


class CvSerializer(serializers.ModelSerializer):
    """Кастомный сериализатор для работы с резюме."""

    class Meta:
        model = Cv
        fields = (
            "title",
            "optional_description",
            "city",
            "salary",
            "experience",
            "currency",
        )


class VacancySerializer(serializers.ModelSerializer):
    """Сериализатор для вакансий."""
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    language = LanguageLevelSerializer(many=True)
    created = serializers.DateTimeField(format='%Y-%m-%d', input_formats=None)

    class Meta:
        model = Vacancy
        fields = (
            "id",
            "author",
            "title",
            "expirience",
            "conditions",
            "grade",
            "work_format",
            "description",
            "requirements",
            "optional_requirements",
            "responsibility",
            "conditions",
            "selection_stages",
            "is_active",
            "is_archive",
            "created",
            "city",
            "min_wage",
            "max_wage",
            "currency",
            "language",
        )

    def validate_title_cv(self, value):
        if match(r'^[-+]?[0-9]+$', value):
            raise ValidationError("Некорректное название вакансии.")
        return value

    def language_create(self, vacancy, languages):
        lang_level = [LanguageLevel(
            vacancy=vacancy,
            language=i['language']['pk'],
            level=i['level'],
        ) for i in languages]
        LanguageLevel.objects.bulk_create(lang_level)

    def create(self, validated_data):
        # author = self.context.get('request').user
        author = User.objects.all()[0]  # авторизации на фронте нет
        languages = validated_data.pop('language')
        vacancy = Vacancy.objects.create(author=author, **validated_data)
        self.language_create(vacancy, languages)
        return vacancy

    def update(self, vacancy, validated_data):
        if languages := validated_data.pop('language', False):  # ЛОВИ МОРЖА!!!
            LanguageLevel.objects.filter(vacancy=vacancy).delete()
            self.language_create(vacancy, languages)
        for attr, value in validated_data.items():
            setattr(vacancy, attr, value)
        return vacancy


class VacancyResponseSerializer(serializers.ModelSerializer):
    status = DisplayChoiceField(choices=VacancyResponse.STATUS)

    class Meta:
        model = VacancyResponse
        fields = ['applicant', 'vacancy', 'status']
