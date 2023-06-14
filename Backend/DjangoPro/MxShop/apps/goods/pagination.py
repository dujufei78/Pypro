#-*- encoding: utf-8 -*-
from rest_framework.pagination import PageNumberPagination


class GoodsPagination(PageNumberPagination):
    '''
    访问第3页，每页2条：http://127.0.0.1:8002/goods/?page=3&page_size=2
    '''
    # 默认每页几条数据
    page_size = 3
    # 可以动态改变每页现实的个数
    page_size_query_param = "page_size"
    # 页码参数
    page_query_param = 'page'
    # 最多能显示多少页
    max_page_size = 100