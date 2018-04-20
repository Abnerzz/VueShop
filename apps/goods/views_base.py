"""
@author: Stephen
@file: views_base.py
@time: 2018/4/18 0018 10:24
"""
from django.http import HttpResponse, JsonResponse

from goods.models import Goods
from django.views.generic.base import View

class GoodsBaseView(View):
    def get(self, request):
        """
        通过django的view实现商品列表页
        :param request:
        :return:
        """
        # json_list = []
        goods = Goods.objects.all()[:10]

        # for good in goods:
        #     json_dict = {}
        #     json_dict["name"] = good.name
        #     json_dict["category"] = good.category.name
        #     json_dict["market_price"] = good.market_price
        #     json_dict["add_time"] = good.add_time
        #
        #     json_list.append(json_dict)

        from django.core import serializers
        json_data = serializers.serialize("json", goods)
        # from django.forms.models import model_to_dict
        # for good in goods:
        #     json_dict = model_to_dict(good)
        #     json_list.append(json_dict)

        import json
        return JsonResponse(json.loads(json_data), safe=False)