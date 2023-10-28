import csv
import json
import random
from datetime import date

import recruitment.settings as ch
from django.core.management.base import BaseCommand
from vacancies.models import Applicant, User, City, Course, Params


class Command(BaseCommand):
    '''Загружает соискателей в БД из applicants.json файла.'''

    def handle(self, *args, **options):
        with open('data/applicants.json', 'rb') as f:
            data = json.load(f)
        cities = City.objects.all()
        courses = Course.objects.all()
        for i in data:
            first_name = i.get('firstName')
            last_name = i.get('lastName')
            username = first_name + last_name
            email = username + '@adm.adm'
            student, status = User.objects.update_or_create(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
            )
            if not Applicant.objects.filter(student=student).exists():
                province = random.choice(cities)
                is_winner = i.get('isWinner')
                age = i.get('age')
                course = random.choice(courses)
                graduation_date = date(random.randint(2018, 2023), random.randint(1, 12), random.randint(1, 27))
                work_format = random.choice(Params.SCHEDULE)[0]
                schedule = random.choice(Params.SCHEDULE)[0]
                contacts = email
                edu_status = random.choice(Applicant.EDU_STATUS)[0]
                work_status = random.choice(Applicant.WORK_STATUS)[0]
                grade = random.choice(ch.GRADE)[0]
                currency = random.choice(ch.CURRENCY)[0]
                Applicant.objects.update_or_create(
                    student=student,
                    province=province,
                    is_winner=is_winner,
                    age=age,
                    course=course,
                    graduation_date=graduation_date,
                    work_format=work_format,
                    schedule=schedule,
                    contacts=contacts,
                    edu_status=edu_status,
                    work_status=work_status,
                    grade=grade,
                    currency=currency,
                )
