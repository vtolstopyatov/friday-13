from recruitment.settings import GRADE
from django_filters import rest_framework as filters
from vacancies.models import Applicant

class ApplicantFilter(filters.FilterSet):
    '''Фильтры для соискателей.'''
    edu_status = filters.CharFilter(
        field_name='edu_status',
    )
    grade = filters.ChoiceFilter(
        choices = GRADE
    )
    work_status = filters.CharFilter(
        field_name='work_status',
    )
    is_winner = filters.NumberFilter(
        field_name='is_winner',
    )
    class Meta:
        model = Applicant
        fields = [
            'edu_status',
            'is_winner',
            'grade',
            'work_status',
            ]