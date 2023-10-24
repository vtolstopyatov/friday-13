import recruitment.settings as ch

from django.db import models
from django.db.models import CheckConstraint, Q, F
from django.contrib.auth import get_user_model

User = get_user_model()


def get_sentinel_user():
    return User.objects.get_or_create(username="deleted")[0]

class Params(models.Model):
    province = models.CharField(max_length=15, verbose_name=("Город"))  # ждём, что фронт скажет, можно связать с моделью регионов https://simplemaps.com/data/ru-cities
    grade = models.CharField(max_length=2, choices=ch.GRADE, verbose_name=("Грейд"))
    is_remote_work = models.BooleanField(default=False, verbose_name=("Удалёнка"))
    min_wage = models.PositiveIntegerField(blank=True, null=True, verbose_name=("Доход от"))
    max_wage = models.PositiveIntegerField(blank=True, null=True, verbose_name=("Доход до"))
    experience = models.CharField(max_length=5, choices=ch.EXP, verbose_name=("Опыт работы"))  # узнать CHOICES у дизайнеров и поменять
    currency = models.CharField(max_length=5, choices=ch.CURRENCY, verbose_name=("Валюта"))  # узнать CHOICES у дизайнеров и поменять
    language = models.CharField(max_length=2, choices=ch.LAN, verbose_name=("Знание языка"))  # узнать CHOICES у дизайнеров и поменять
    language_level = models.CharField(max_length=2, choices=ch.LAN_LVL, verbose_name=("Уровень языка"))

    class Meta:
        abstract = True


class Vacancy(Params):
    '''Модель вакансий.'''
    # уточнить обязательные поля у дизайнеров
    # проверка полей wage_gt wage_lt
    # проверка полей is_active is_archive
    author = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user), verbose_name=("Рекрутер"))  # лучше чтобы вакансия осталась у студентов при удалении рекрутера. Протестировать это
    name = models.CharField(max_length=200, null=False, verbose_name=("Название"))
    description = models.TextField(verbose_name=("Подробности"))
    requirements = models.TextField(verbose_name=("Требования"))
    optional_requirements = models.TextField(verbose_name=("Необязательные требования"))
    responsibility = models.TextField(verbose_name=("Обязанности"))
    conditions = models.TextField(verbose_name=("Условия"))
    selection_stages = models.TextField(verbose_name=("Этапы отбора"))
    is_active = models.BooleanField(default=True, verbose_name=("Опубликована"))
    is_archive = models.BooleanField(default=False, verbose_name=("Архивная"))
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            CheckConstraint(
                check=Q(min_wage__lte=F('max_wage')),  # добавить проверку нуля
                name='check_min_wage_less_than_max_wage',
            ),
        ]


class Cv(Params): 
    name = models.CharField(max_length=200, null=False, verbose_name=("Название"))
    optional_description = models.TextField(verbose_name=("Немного о себе"))