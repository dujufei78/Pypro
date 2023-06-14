#-*- encoding: utf-8 -*-
from django.contrib.auth import get_user_model

from rest_framework import serializers
User = get_user_model()

class UserRegSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'mobile')

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'gender', 'birthday', 'email', 'mobile')
