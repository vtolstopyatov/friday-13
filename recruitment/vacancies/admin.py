from django.contrib import admin
from .models import Vacancy, City, Language, LanguageLevel

admin.site.register(Vacancy)
admin.site.register(City)
admin.site.register(Language)
admin.site.register(LanguageLevel)
