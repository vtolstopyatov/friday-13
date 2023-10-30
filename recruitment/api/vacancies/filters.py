from recruitment.settings import GRADE
from django_filters import rest_framework as filters
from vacancies.models import Vacancy


class VacancyFilter(filters.FilterSet):
    """
    Фильтры для вакансий.
    """
    
    city = filters.CharFilter(
        field_name='city',
    )
    grade = filters.ChoiceFilter(
        choices=GRADE
    )
    is_remote_work = filters.CharFilter(
        field_name='is_remote_work',
    )
    min_wage = filters.NumberFilter(
        field_name='min_wage',
    )
    max_wage = filters.NumberFilter(
        field_name='max_wage',
    )
    is_active = filters.BooleanFilter()

    class Meta:
        model = Vacancy
        fields = [
            'grade',
            'city',
            'is_remote_work',
            'min_wage',
            'max_wage',
            'is_active',
        ]
