from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from goods.filters import GoodsFilter
from goods.models import Goods
from goods.serializers import GoodsSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, mixins, generics
from rest_framework.pagination import PageNumberPagination

# Create your views here.
class GoodsResultPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"


class GoodsListView(generics.ListAPIView):
    """
    商品列表页
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsResultPagination
    filter_backends = (DjangoFilterBackend,)
    filter_class = GoodsFilter


'''
    # use APIView
    
    
    class GoodsListView(APIView):
    """
    List goods
    """
    def get(self, request, format=None):
        goods = Goods.objects.all()[:10]
        goods_serializer = GoodsSerializer(goods, many=True)
        return Response(goods_serializer.data)

    def post(self, request):
        serializer = GoodsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''
