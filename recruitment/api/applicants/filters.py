from ...recruitment import settings as ch
from django_filters import rest_framework as filters
from vacancies.models import Applicant

class ApplicantFilter(filters.FilterSet):
    '''Фильтры для соискателей.'''
    edu_status = filters.ChoiceFilter(
        choices = ch.EDU_STATUS
    )
    grade = filters.ChoiceFilter(
        choices = ch.GRADE
    )
    work_status = filters.ChoiceFilter(
        choices = ch.WORK_STATUS
    )
    is_winner = filters.NumberFilter(
        field_name='is_winner',
    )
    province = filters.CharFilter(
        field_name='province__name'
    )
    expirience = filters.DateFilter(
        field_name='expirience__date_start'
    )
    work_format = filters.ChoiceFilter(
        choices = ch.WORK_FORMAT
    )
    class Meta:
        model = Applicant
        fields = [
            'edu_status',
            'is_winner',
            'grade',
            'work_status',
            'province',
            'expirience',
            'work_format',
            ]