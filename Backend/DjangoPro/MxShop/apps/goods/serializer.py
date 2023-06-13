# -*- encoding: utf-8 -*-
from goods.models import Goods, GoodsCategory
from rest_framework import serializers

from goods.models import GoodsImage


class CategorySerializer3(serializers.ModelSerializer):
    '''
    商品三级分类序列化
    '''

    class Meta:
        model = GoodsCategory
        fields = '__all__'


class CategorySerializer2(serializers.ModelSerializer):
    '''
    商品二级分类序列化
    '''
    # 在parent_category字段里定义related_name='sub_cat'
    sub_cat = CategorySerializer3(many=True)

    class Meta:
        model = GoodsCategory
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    '''
    商品一级类别序列化
    '''
    sub_cat = CategorySerializer2(many=True)

    class Meta:
        model = GoodsCategory
        fields = '__all__'


class GoodsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsImage
        fields = ('image', )


class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    # images字段是在GoodsImage里goods字段里设置的related_name="images"
    images = GoodsImageSerializer(many=True)

    class Meta:
        model = Goods
        fields = '__all__'
