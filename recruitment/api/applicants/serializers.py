from rest_framework import serializers
from vacancies.models import Applicant, VacancyResponse, Expirience
class ExpirienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expirience
        fields = [
            'date_start',
            'date_end',
            'company',
            'title',
            'description',
        ]

class VacancyResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacancyResponse
        fields = [
            'status'
        ]

class ApplicantSerializer(serializers.ModelSerializer):
    '''Сериалайзер соискателей.'''
    first_name = serializers.ReadOnlyField(source='student.first_name')
    last_name = serializers.ReadOnlyField(source='student.last_name')
    avatar_url = serializers.ImageField(source='student.userpic', read_only=True, use_url=True)
    course = serializers.ReadOnlyField(source='course.name')
    city = serializers.ReadOnlyField(source='province.name')
    response_count = serializers.SerializerMethodField()
    test_task_count = serializers.SerializerMethodField()
    interview_count = serializers.SerializerMethodField()
    work_format = serializers.CharField(source='get_work_format_display')
    work_status = serializers.CharField(source='get_work_status_display')
    edu_status = serializers.CharField(source='get_edu_status_display')
    grade = serializers.CharField(source='get_grade_display')
    expirience = ExpirienceSerializer()
    response_status = VacancyResponseSerializer()

    class Meta:
        model = Applicant
        fields = [
            'id',
            'first_name',
            'last_name',
            'contacts',
            'optional_description',
            'avatar_url',
            'is_winner',
            'city',
            'age',
            'course',
            'graduation_date',
            'salary',
            'work_format',
            'grade',
            'work_status',
            'edu_status',
            'response_count',
            'test_task_count',
            'interview_count',
            'expirience',
            'response_status'
        ]

    def get_response_count(self, obj):
        return obj.vacancy_responses.count()

    def get_test_task_count(self, obj):
        return obj.vacancy_test_tasks.count()

    def get_interview_count(self, obj):
        return obj.vacancy_interviews.count()
