from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from goods.filter import GoodsFilter
from goods.pagination import GoodsPagination
from rest_framework.response import Response

from rest_framework.views import APIView

from goods.models import Goods, GoodsCategory
from goods.serializer import GoodsSerializer, CategorySerializer
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin

from rest_framework.viewsets import GenericViewSet


class GoodsListView(APIView):
    def get(self, request):
        goods = Goods.objects.all()
        serializer = GoodsSerializer(goods, many=True)
        return Response(serializer.data)


class GoodsListViewSet(ListModelMixin, RetrieveModelMixin, CreateModelMixin, GenericViewSet):
    '''
    商品列表数据展示（这句话在注释里，可以编辑） \n
    category：可显示三级菜单 \n
    images: 显示商品轮播图，商品---轮播图是"一对多关系" \n
    
    '''
    queryset = Goods.objects.all().order_by('id')
    serializer_class = GoodsSerializer
    # 自定义分页
    pagination_class = GoodsPagination

    # 自定义过滤
    # URL：/goods/?price_min=10&price_max=70
    # 配置过滤、搜索、排序
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = GoodsFilter

    # 搜索功能
    # =表示精准搜索
    search_fields = ('=name', 'goods_brief')

    # 排序功能
    ordering_fields = ('sold_num', 'add_time')


class CategoryViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    '''
    list: 商品分类列表数据
    '''
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer
