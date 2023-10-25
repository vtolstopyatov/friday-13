import recruitment.settings as ch

from django.db import models
from django.db.models import CheckConstraint, UniqueConstraint, Q, F
from django.contrib.auth import get_user_model

User = get_user_model()


def get_sentinel_user():
    return User.objects.get_or_create(username="deleted")[0]


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='Город')
    region = models.CharField(max_length=50, verbose_name='Регион')
    country = models.CharField(max_length=50, verbose_name='Страна')


class Language(models.Model):
    language = models.CharField(max_length=50, verbose_name='Язык')


class Params(models.Model):
    grade = models.CharField(max_length=2, choices=ch.GRADE, verbose_name=("Грейд"))
    is_remote_work = models.BooleanField(default=False, verbose_name=("Удалёнка"))
    min_wage = models.PositiveIntegerField(verbose_name=("Доход от"))
    max_wage = models.PositiveIntegerField(verbose_name=("Доход до"))
    experience = models.CharField(max_length=5, choices=ch.EXP, verbose_name=("Опыт работы"))  # узнать CHOICES у дизайнеров и поменять
    currency = models.CharField(max_length=5, choices=ch.CURRENCY, verbose_name=("Валюта"))  # узнать CHOICES у дизайнеров и поменять

    class Meta:
        abstract = True


class Vacancy(Params):
    '''Модель вакансий.'''
    # уточнить обязательные поля у дизайнеров
    # проверка полей is_active is_archive
    province = models.ForeignKey(City, on_delete=models.PROTECT, related_name='vacancy', verbose_name='Город')
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
                check=Q(min_wage__lte=F('max_wage')) | Q(max_wage__exact=0),
                name='check_min_wage_less_than_max_wage',
            ),
        ]


class LanguageLevel(models.Model):
    LANG_LVL = [
        ("A1", "A1"),
        ("A2", "A2"),
        ("B1", "B1"),
        ("B2", "B2"),
        ("C1", "C1"),
        ("C2", "C2"),
    ]
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='language')
    level = models.CharField(max_length=2, choices=LANG_LVL)

    class Meta:
        unique_together = ('language', 'vacancy', 'level')


class Cv(Params):
    province = models.ForeignKey(City, on_delete=models.PROTECT, related_name='cv', verbose_name='Город')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=("Рекрутер"))
    name = models.CharField(max_length=200, null=False, verbose_name=("Название"))
    optional_description = models.TextField(verbose_name=("Немного о себе"))
