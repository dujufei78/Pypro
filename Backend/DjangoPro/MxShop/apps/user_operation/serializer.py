#-*- encoding: utf-8 -*-
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from user_operation.models import UserFav


class UserFavsSerializer(serializers.ModelSerializer):
    # 获取当前用户
    # user = serializers.HiddenField(
    #     default=serializers.CurrentUserDefault()
    # )

    class Meta:
        # validate实现唯一联合，一个商品只能收藏一次
        validators= [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields = ('user', 'goods'),
                message='已经收藏，别客气'
            )
        ]
        model = UserFav
        fields = ('user', 'goods', 'id')