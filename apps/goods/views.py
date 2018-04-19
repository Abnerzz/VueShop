from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from goods.filters import GoodsFilter
from goods.models import Goods, GoodsCategory
from goods.serializers import GoodsSerializer, CategorySerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, mixins, generics, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters


# Create your views here.
class GoodsResultPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"


class GoodsListViewSet(generics.ListAPIView, viewsets.GenericViewSet):
    """
    商品列表页,分页，搜索，过滤，排序
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsResultPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = GoodsFilter
    search_fields = ("name", "goods_brief")
    ordering_fields = ('sold_num', 'add_time')


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        商品分类列表数据
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer
