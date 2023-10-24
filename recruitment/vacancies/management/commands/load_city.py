import csv

from django.core.management.base import BaseCommand
from vacancies.models import City


class Command(BaseCommand):
    '''Загружает ингредиенты в БД из ingredients.json файла.'''

    def handle(self, *args, **options):
        with open('data/towns.csv', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader[1:]:
                City.objects.update_or_create(
                    name=row[0],
                    region=row[1],
                    country=row[2],
                )

# Vacancy.objects.create(
#     author=User.objects.get(pk=1),
#     name='ognbawopngp',
#     description='ognbawopngp',
#     requirements='ognbawopngp',
#     optional_requirements='ognbawopngp',
#     responsibility='ognbawopngp',
#     conditions='ognbawopngp',
#     selection_stages='ognbawopngp',
#     is_active=True,
#     is_archive=False,
#     created='ognbawopngp',
#     province = City.objects.get_or_create(name='a', region='a', country='a')[0],
#     grade = 'JN',
#     is_remote_work = False,
#     min_wage = 0,
#     max_wage = 0,
#     experience = 'LOW',
#     currency = 'RUB',
#     language = 'RU',
#     language_level = 'A1',))