from django_filters import rest_framework as filters
from .models import Art

class ArtsFilter(filters.FilterSet):
    category = filters.CharFilter(field_name='category__name', lookup_expr='icontains')
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Art
        fields = (
            'category',
            'title'
            )