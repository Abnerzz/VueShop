"""
@author: Stephen
@file: serializer.py
@time: 2018/4/18 0018 14:43
"""
from rest_framework import serializers
from goods.models import Goods, GoodsCategory

'''
class GoodsSerializer(serializers.Serializer):
    """

    """
    name = serializers.CharField(required=True, max_length=100)
    click_num = serializers.IntegerField(default=0)
    goods_front_image = serializers.ImageField()

    def create(self, validated_data):
        """
        :param validated_data:
        :return:
        """
        return Goods.objects.create(**validated_data)
'''

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        # fields = "__all__"
        fields = ("__all__")

class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Goods
        # fields = ("name", "click_num", "market_price", "add_time")
        fields = "__all__"