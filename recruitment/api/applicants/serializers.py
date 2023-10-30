from rest_framework import serializers
from vacancies.models import Applicant, Expirience, VacancyResponse


class ExpirienceSerializer(serializers.ModelSerializer):
    """
    Сериалайзер опыта кандидата.
    """

    class Meta:
        model = Expirience
        fields = [
            "date_start",
            "date_end",
            "company",
            "title",
            "description",
        ]


class ApplicantSerializer(serializers.ModelSerializer):
    """
    Сериалайзер соискателей.
    """

    first_name = serializers.ReadOnlyField(source="student.first_name")
    last_name = serializers.ReadOnlyField(source="student.last_name")
    avatar_url = serializers.ImageField(
        source="student.userpic", read_only=True, use_url=True
    )
    course = serializers.ReadOnlyField(source="course.name")
    city = serializers.ReadOnlyField(source="province.name")
    response_count = serializers.SerializerMethodField()
    work_format = serializers.CharField(source="get_work_format_display")
    work_status = serializers.CharField(source="get_work_status_display")
    edu_status = serializers.CharField(source="get_edu_status_display")
    grade = serializers.CharField(source="get_grade_display")
    expirience = ExpirienceSerializer(source="exp")

    class Meta:
        model = Applicant
        fields = [
            "id",
            "first_name",
            "last_name",
            "contacts",
            "optional_description",
            "avatar_url",
            "is_winner",
            "city",
            "age",
            "course",
            "graduation_date",
            "salary",
            "work_format",
            "grade",
            "work_status",
            "edu_status",
            "response_count",
            "test_task_count",
            "interview_count",
            "expirience",
        ]

    def get_response_count(self, obj):
        return obj.vacancy_responses.count() + obj.response_base_count


class VacancyApplicantSerializer(ApplicantSerializer):
    """
    Сериалайзер статуса соискателей.
    """

    response_status = serializers.SerializerMethodField()

    class Meta:
        model = Applicant
        fields = [
            "id",
            "first_name",
            "last_name",
            "contacts",
            "optional_description",
            "avatar_url",
            "is_winner",
            "city",
            "age",
            "course",
            "graduation_date",
            "salary",
            "work_format",
            "grade",
            "work_status",
            "edu_status",
            "response_count",
            "test_task_count",
            "interview_count",
            "expirience",
            "response_status",
        ]

    def get_response_status(self, obj, *args, **kwargs):
        vacancy_pk = (
            self.context.get("request")
            .parser_context.get("kwargs")
            .get("vacancy_pk")
        )
        status = VacancyResponse.objects.get(
            applicant=obj.pk, vacancy=vacancy_pk
        ).status
        return VacancyResponse.STATUS[status - 1][1]
