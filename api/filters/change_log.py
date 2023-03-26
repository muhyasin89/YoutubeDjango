from apps.change_log.models import ChangeLog
from django_filters import rest_framework as filters

class ChangeLogFilter(filters.FilterSet):
    min_created = filters.NumberFilter(field_name="created", lookup_expr='gte')

    class Meta:
        model = ChangeLog
        fields = ['section_status', 'created']
