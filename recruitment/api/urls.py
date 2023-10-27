from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from .vacancies.views import VacancyViewSet
from .cities.views import CityViewSet
from .applicants.views import ApplicantViewSet
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

v1_router = routers.DefaultRouter()

v1_router.register('vacancies', VacancyViewSet, basename='vacancies')
v1_router.register('cities', CityViewSet, basename='cities')
v1_router.register('applicants', ApplicantViewSet, basename='applicants')

urlpatterns = [
    path('', include(v1_router.urls)),
]

schema_view = get_schema_view(
   openapi.Info(
      title="Friday-13 API",
      default_version='v1',
      description="Документация для API команды Friday-13",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    url('swagger<format>/',
         schema_view.without_ui(cache_timeout=0),
         name='schema-json'),
    url('swagger/', schema_view.with_ui(
         'swagger', cache_timeout=0),
         name='schema-swagger-ui',),
    url('redoc/',
         schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
]

urlpatterns += staticfiles_urlpatterns()
