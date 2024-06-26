from django_filters import rest_framework as filters
from .models import Art

class ArtsFilter(filters.FilterSet):
    category = filters.CharFilter(field_name='category__name', lookup_expr='icontains')
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    author_id = filters.NumberFilter(field_name='author__id', lookup_expr='iexact')
    author_name = filters.CharFilter(field_name='author__name', lookup_expr='icontains')

    class Meta:
        model = Art
        fields = (
            'category',
            'title',
            'author'
            )