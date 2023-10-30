from django.contrib import admin
from .models import Vacancy, City, Language, LanguageLevel, Applicant, Course, VacancyResponse, Expirience

admin.site.register(Vacancy)
admin.site.register(City)
admin.site.register(Language)
admin.site.register(LanguageLevel)
admin.site.register(Applicant)
admin.site.register(Course)
admin.site.register(VacancyResponse)
admin.site.register(Expirience)
