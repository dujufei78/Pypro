"""BookManage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app01 import views

urlpatterns = [
    # 登陆注册
    path('login/', views.login),
    path('index/', views.index),
    path('register/', views.register),
    path('logout/', views.logout),

    # curd书籍-原始的CURD
    path('book_list/', views.book_list),
    path('book_add/', views.book_add),
    path('book_edit/', views.book_edit),
    path('book_del/<id>', views.book_del),

]
