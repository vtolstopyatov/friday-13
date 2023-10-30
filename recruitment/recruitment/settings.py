import os
from datetime import timedelta
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = (
    "django-insecure-g4$9ub=hdp)+3$@qqy&c0r#s6fr2_!&+&vg&)m4vxjek#*mwli"
)

DEBUG = True

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "130.193.38.180",
    "aboba.pro",
]

CSRF_TRUSTED_ORIGINS = [
    "https://aboba.pro",
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://aboba.pro",
    "https://hakaton-tracker-team-13.vercel.app",
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_filters",
    "drf_yasg",
    "corsheaders",
    "users.apps.UsersConfig",
    "api.apps.ApiConfig",
    "vacancies.apps.VacanciesConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "recruitment.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "recruitment.wsgi.application"


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": os.getenv(
            "DB_ENGINE", default="django.db.backends.postgresql"
        ),
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
    # 'DEFAULT_AUTHENTICATION_CLASSES': [
    #     'rest_framework.authentication.TokenAuthentication',
    #     'rest_framework.authentication.BasicAuthentication',
    #     'rest_framework.authentication.SessionAuthentication',
    # ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
}

ACTIVATION_URL = os.getenv("ACTIVATION_URL")

DJOSER = {
    "HIDE_USERS": False,
    "LOGIN_FIELD": "email",
    "SERIALIZERS": {
        "user_create": "users.serializers.CustomUserCreateSerializer",
        "user": "users.serializers.CustomUserSerializer",
        "current_user": "users.serializers.CustomUserSerializer",
    },
    "ACTIVATION_URL": "api/account-activate/{uid}/{token}/",
    "SEND_ACTIVATION_EMAIL": True,
    # Это нужно будет согласовывать с фронтом: они должны будут принять эту
    # ссылку и вывести экран для ввода нового пароля, который вместе с uid и
    # token улетит на password_reset_confirm
    # "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    # "PASSWORD_RESET_CONFIRM_URL": "api/password-change/{uid}/{token}",
    # "USERNAME_CHANGED_EMAIL_CONFIRMATION": True,
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "AUTH_HEADER_TYPES": ("Bearer",),
}

AUTH_USER_MODEL = "users.CustomUser"

GRADE = [
    ("IN", "Intern"),
    ("JR", "Junior"),
    ("MD", "Middle"),
    ("SR", "Senior"),
    ("LD", "Lead"),
]

EXP = [
    ("LOW", "0"),
    ("MED", "1-3"),
    ("HI", "3-6"),
    ("HIP", "6+"),
]

CURRENCY = [
    ("RUB", "₽"),
    ("DOL", "$"),
    ("EURO", "€"),
    ("UAH", "₴"),
]

LAN = [
    ("RU", "Русский"),
    ("EU", "English"),
    ("UA", "Украинский"),
]

LAN_LVL = [
    ("A1", ""),
    ("A2", ""),
    ("B1", ""),
    ("B2", ""),
    ("C1", ""),
    ("C2", ""),
]

EDU_STATUS = [
    (1, "Студент"),
    (2, "Выпускник"),
]
WORK_STATUS = [
    (1, "Учебный"),
    (2, "Релевантный"),
    (3, "Около-релевантный"),
]
FULL_DAY = "FD"
HYBRID = "HB"
REMOTE = "RM"
FLEX = "FX"
WORK_FORMAT = [
    (FULL_DAY, "Полный день"),
    (HYBRID, "Гибрид"),
    (REMOTE, "Удалённая работа"),
    (FLEX, "Гибкий график"),
]
