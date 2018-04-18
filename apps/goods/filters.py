"""
@author: Stephen
@file: filters.py
@time: 2018/4/18 0018 17:55
"""

import django_filters
from goods.models import Goods

class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品的过滤类
    """
    min_price = django_filters.NumberFilter(name="price", lookup_expr="gte")
    max_price = django_filters.NumberFilter(name="price", lookup_expr="lte")

    class Meta:
        model = Goods
        fields = ['min_price', 'max_price']
