from django_filters import rest_framework as filters

from app_service.models import Link


class LinkFilter(filters.FilterSet):
    class Meta:
        model = Link
        fields = ("id", "link_code", "domain_zone")
