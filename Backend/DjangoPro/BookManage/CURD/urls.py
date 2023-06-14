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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path

from CURD import views

urlpatterns = [
    # 练习CURD----GenericAPIView版增删改查
    url('Book_GenericAPIView/', views.Book_GenericAPIView.as_view()),
    url('Book_GenericAPIView/(?P<pk>\d+)/', views.BookSingle_GenericAPIView.as_view()),
    
    # 练习CURD----APIView版增删改查
    url('^books/$', views.Book_APIView.as_view()),
    url('books/(?P<pk>\d+)/', views.BookDetail_APIView.as_view()),
]
