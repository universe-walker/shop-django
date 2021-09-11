import django_filters

from .models import Product, Characteristic


class ProductFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter(field_name='price')
    characteristic = django_filters.ModelMultipleChoiceFilter(
        queryset=Characteristic.objects.none(), label='Характеристики')

    class Meta:
        model = Product
        fields = ['rating']
