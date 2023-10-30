from django.urls import include, path
from .vacancies.views import VacancyViewSet, ResponsesViewSet
from .cities.views import CityViewSet
from .applicants.views import ApplicantViewSet
from .languages.views import LanguageViewSet
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework_nested import routers

v1_router = routers.SimpleRouter()

v1_router.register("vacancies", VacancyViewSet, basename="vacancies")
v1_router.register("cities", CityViewSet, basename="cities")
v1_router.register("applicants", ApplicantViewSet, basename="applicants")
v1_router.register("languages", LanguageViewSet, basename="languages")

vacancies_router = routers.NestedSimpleRouter(
    v1_router,
    "vacancies",
    lookup="vacancy",
)
vacancies_router.register(
    "responses",
    ResponsesViewSet,
    basename="vacancy-responses",
)

schema_view = get_schema_view(
    openapi.Info(
        title="Friday-13 API",
        default_version="v1",
        description="Документация для API команды Friday-13",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("", include(v1_router.urls)),
    path("", include(vacancies_router.urls)),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]

urlpatterns += staticfiles_urlpatterns()
