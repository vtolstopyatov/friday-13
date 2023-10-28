import csv
import json

from django.core.management.base import BaseCommand
from vacancies.models import City


class Command(BaseCommand):
    '''Загружает города в БД из towns.csv файла.'''

    def handle(self, *args, **options):
        with open('data/towns.csv', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                City.objects.update_or_create(
                    name=row[0],
                    region=row[1],
                    country=row[2],
                )
