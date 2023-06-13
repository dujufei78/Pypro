# -*- encoding: utf-8 -*-
from rest_framework import serializers

from app01.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
    
    publish_name = serializers.SerializerMethodField(source='publish.name')
    publich_addr = serializers.SerializerMethodField(source='publich.addr')

    authorlist = serializers.SerializerMethodField()

    def get_authorlist(self, obj):
        res = []
        for i in obj.authorlist.all():
            res.append({'name': i['name'], 'age': i['age']})
        return res
