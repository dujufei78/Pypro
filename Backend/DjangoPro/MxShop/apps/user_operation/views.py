from django.shortcuts import render

# Create your views here.
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet
from user_operation.models import UserFav
from user_operation.serializer import UserFavsSerializer


class UserFavsViewSet(ListModelMixin, CreateModelMixin, DestroyModelMixin, GenericViewSet):
    '''
    
    '''
    queryset = UserFav.objects.all()
    serializer_class = UserFavsSerializer