from django.db import models
from django.db.models import CheckConstraint, Q, F
from django.contrib.auth import get_user_model

User = get_user_model()


def get_sentinel_user():
    return User.objects.get_or_create(username="deleted")[0]


class Vacancy(models.Model):
    '''Модель вакансий.'''
    CHOICES = [
        ("JR", "Junior"),
        ("MD", "Middle"),
        ("SR", "Senior"),
    ]
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
    # ↓ пересекаются с резюме. Разбить все на отдельные модели? Вынести в другую и наследоваться? ↓ 
    province = models.CharField(verbose_name=("Город"))  # ждём, что фронт скажет, можно связать с моделью регионов https://simplemaps.com/data/ru-cities
    grade = models.CharField(choices=CHOICES, verbose_name=("Грейд"))
    is_remote_work = models.BooleanField(default=False, verbose_name=("Удалёнка"))
    min_wage = models.PositiveIntegerField(blank=True, null=True, verbose_name=("Доход от"))
    max_wage = models.PositiveIntegerField(blank=True, null=True, verbose_name=("Доход до"))
    experience = models.CharField(choices=CHOICES, verbose_name=("Опыт работы"))  # узнать CHOICES у дизайнеров и поменять
    currency = models.CharField(choices=CHOICES, verbose_name=("Валюта"))  # узнать CHOICES у дизайнеров и поменять
    language = models.CharField(choices=CHOICES, verbose_name=("Знание языка"))  # узнать CHOICES у дизайнеров и поменять
    language_level = models.CharField(choices=CHOICES, verbose_name=("Уровень языка"))  # узнать CHOICES у дизайнеров и поменять

    class Meta:
        constraints = [
            CheckConstraint(
                check=Q(min_wage__lte=F('max_wage')),  # добавить проверку нуля
                name='check_min_wage_less_than_max_wage',
            ),
        ]
