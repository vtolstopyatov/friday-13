from rest_framework import serializers
from vacancies.models import Applicant


class ApplicantSerializer(serializers.ModelSerializer):
    '''Сериалайзер соискателей.'''
    first_name = serializers.ReadOnlyField(source='student.first_name')
    last_name = serializers.ReadOnlyField(source='student.last_name')
    avatar_url = serializers.ImageField(source='student.userpic', read_only=True, use_url=True)
    course = serializers.ReadOnlyField(source='course.name')
    city = serializers.ReadOnlyField(source='city.name')
    response_count = serializers.SerializerMethodField()
    test_task_count = serializers.SerializerMethodField()
    interview_count = serializers.SerializerMethodField()
    schedule = serializers.CharField(source='get_schedule_display')

    class Meta:
        model = Applicant
        fields = [
            'id',
            'first_name',
            'last_name',
            'avatar_url',
            'is_winner',
            'city',
            'age',
            'course',
            'graduation_date',
            'schedule',
            'response_count',
            'test_task_count',
            'interview_count',
        ]

    def get_response_count(self, obj):
        return obj.vacancy_responses.count()

    def get_test_task_count(self, obj):
        return obj.vacancy_test_tasks.count()

    def get_interview_count(self, obj):
        return obj.vacancy_interviews.count()
