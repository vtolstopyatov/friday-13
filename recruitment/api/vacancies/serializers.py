from re import match
from rest_framework import serializers

from rest_framework.serializers import ValidationError

from vacancies.models import Cv, Vacancy


class CvCreateSerializer(serializers.ModelSerializer):
    """Кастомный сериализатор для создания резюме."""

    class Meta:
        model = Cv
        fields = (
            "name",
            "optional_description",
            "province",
            "is_remote_work",
            "min_wage",
            "max_wage",
            "experience",
            "currency",
            "language",
            "language_level",
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
            "name",
            "optional_description",
            "province",
            "is_remote_work",
            "min_wage",
            "max_wage",
            "experience",
            "currency",
            "language",
            "language_level",
        )


class VacancyCreateSerializer(serializers.ModelSerializer):
    """Кастомный сериализатор для создания вакансии."""

    class Meta:
        model = Vacancy
        fields = (
            "author",
            "name",
            "description",
            "requirements",
            "experience",
            "optional_requirements",
            "responsibility",
            "conditions",
            "selection_stages",
            "is_active",
            "is_archive",
            "created",

            "province",
            "is_remote_work",
            "min_wage",
            "max_wage",
            "experience",
            "currency",
            "language",
            "language_level",
        )

    def validate_name_cv(self, value):
        if match(r'^[-+]?[0-9]+$', value):
            raise ValidationError("Некорректное название вакансии.")
        return value

    def create(self, validated_data):
        author = self.context.get('request').user
        vacancy = Vacancy.objects.create(author=author, **validated_data)
        return vacancy


class VacancySerializer(serializers.ModelSerializer):
    """Кастомный сериализатор для работы с вакансией."""

    class Meta:
        model = Vacancy
        fields = (
            "author",
            "name",
            "description",
            "requirements",
            "experience",
            "optional_requirements",
            "responsibility",
            "conditions",
            "selection_stages",
            "is_active",
            "is_archive",
            "created",

            "province",
            "is_remote_work",
            "min_wage",
            "max_wage",
            "experience",
            "currency",
            "language",
            "language_level",
        )
