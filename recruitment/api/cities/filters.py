from django_filters import rest_framework as filters
from vacancies.models import City


class CityFilter(filters.FilterSet):
    """
    Фильтры для городов.
    """

    name = filters.CharFilter(
        field_name="name",
        lookup_expr="icontains",
    )

    class Meta:
        model = City
        fields = ["name"]
