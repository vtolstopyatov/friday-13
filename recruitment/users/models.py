from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """Кастомный менеджер юзеров."""

    def create_user(self, email, username, role=None, password=None, **others):
        if not email:
            raise ValueError(_("У пользователя должен быть указан email"))

        validate_password(password)

        user = self.model(
            email=self.normalize_email(email), username=username, **others
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **others):
        user = self.model(email=self.normalize_email(email), username=username)
        user.is_superuser = True
        user.is_staff = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    """Основная модель пользователя."""

    DEFAULT_STATUS = "В сети"
    MALE = "male"
    FEMALE = "female"
    ROLE_CHOICES = [
        (MALE, "Мужской"),
        (FEMALE, "Женский"),
    ]

    username_validator = UnicodeUsernameValidator()
    objects = CustomUserManager()

    first_name = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Имя"),
        help_text=_("Введите имя"),
    )
    last_name = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Фамилия"),
        help_text=_("Введите фамилию"),
    )
    email = models.EmailField(
        verbose_name=_("E-mail"),
        help_text=_("Введите ваш e-mail"),
        unique=True,
    )
    username = models.CharField(
        max_length=100,
        unique=True,
        verbose_name=_("Логин"),
        help_text=_("Введите логин"),
        validators=[username_validator],
    )
    userpic = models.ImageField(
        upload_to="uploads/%Y/%m/%d/",
        validators=[
            FileExtensionValidator(allowed_extensions=["jpeg", "jpg", "png"])
        ],
        verbose_name=_("Фото пользователя"),
        help_text=_("Выберите изображение"),
        blank=True,
        null=True,
    )
    gender = models.CharField(
        max_length=50,
        choices=ROLE_CHOICES,
        verbose_name=_("Пол"),
        help_text=_("Укажите ваш пол"),
        default=MALE,
    )
    start_datetime = models.DateTimeField(auto_now_add=True)
    last_datetime = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("username",)


    class Meta:
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")

    def __str__(self):
        return self.username
