# -*- encoding: utf-8 -*-
import django_filters
from django.db.models import Q

from goods.models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    '''
    过滤商品的类
    '''
    # name是要过滤的字段，lookup_expr是执行的动作
    price_min = django_filters.NumberFilter(name='shop_price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(name='shop_price', lookup_expr='lte')
    top_category = django_filters.NumberFilter(name='category', method='top_category_filter')
    # Q查询表示"或者", 不管当前点击1、2、3级分类，都能找到
    def top_category_filter(self, queryset, name, value):
        return queryset.filter(Q(category_id=value) |
                               Q(category_parent_category_id=value) |
                               Q(category_parent_category_parent_category_id=value))

    class Meta:
        model = Goods
        # 设置is_hot=True ，过滤热卖商品字段
        fields = ['price_min', 'price_max', 'is_hot']
