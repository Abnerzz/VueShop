"""
@author: Stephen
@file: filters.py
@time: 2018/4/18 0018 17:55
"""

import django_filters
from django.db.models import Q
from goods.models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品的过滤类
    """
    pricemin = django_filters.NumberFilter(name="shop_price", lookup_expr="gte")
    pricemax = django_filters.NumberFilter(name="shop_price", lookup_expr="lte")
    top_category = django_filters.NumberFilter(method='top_category_filter')

    def top_category_filter(self, queryset, name, value):
        queryset = queryset.filter(Q(category_id=value)|Q(category__parent_category_id=value)|Q(category__parent_category__parent_category_id=value))

    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemax', 'name']
