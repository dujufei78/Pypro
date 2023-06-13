"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.urls import path, re_path
from django.views.static import serve
from rest_framework_jwt.views import obtain_jwt_token

from rest_framework.authtoken import views

from goods.views import GoodsListViewSet, GoodsListView, CategoryViewSet
from rest_framework.routers import DefaultRouter

from rest_framework.documentation import include_docs_urls

import xadmin
from MxShop.settings import MEDIA_ROOT
from user_operation.views import UserFavsViewSet

router = DefaultRouter()

# 配置goods的url
router.register(r'goods', GoodsListViewSet, base_name='goods')
# 配置category的url
router.register(r'categorys', CategoryViewSet, base_name='categorys')
# 用户收藏url
router.register(r'userfavs', UserFavsViewSet, base_name='userfavs')

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # 这里使用xadmin,比admin更加的功能强大
    re_path('^xadmin/', xadmin.site.urls),
    re_path('^ueditor/', include('DjangoUeditor.urls')),

    # 文件
    re_path('media/<path:path>', serve, {'document_root': MEDIA_ROOT}),

    # drf文档，title自定义
    path('docs', include_docs_urls(title='MEM管理')),
    path('api-auth', include('rest_framework.urls')),

    # APIView写法
    # path('goods/', GoodsListView.as_view())

    # 使用router自动配置url
    re_path('^', include(router.urls)),

    # drf-token
    # path('api-token-auth/', views.obtain_auth_token),
    # jwt的token认证接口
    path('jwt-token/', obtain_jwt_token)

]
