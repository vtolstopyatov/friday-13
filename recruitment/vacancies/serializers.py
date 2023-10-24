import base64
from re import match

from django.conf import settings
from django.core.files.base import ContentFile
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework.serializers import (CurrentUserDefault, HiddenField,
                                        ImageField, ModelSerializer,
                                        ValidationError)

from .models import Cv, Vacancy


class CvCreateSerializer(UserCreateSerializer):
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


class CvSerializer(UserSerializer):
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

class VacancyCreateSerializer(UserCreateSerializer):
    """Кастомный сериализатор для создания вакансии."""

    class Meta:
        model = Cv
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


class CvSerializer(UserSerializer):
    """Кастомный сериализатор для работы с вакансией."""

    class Meta:
        model = Cv
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