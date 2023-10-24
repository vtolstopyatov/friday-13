from django.urls import include, path, url
from rest_framework import routers
from .views import VacancyViewSet
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

v1_router = routers.DefaultRouter()

v1_router.register('recipes', VacancyViewSet, basename='vacancy')

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
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),
]

urlpatterns += staticfiles_urlpatterns()
