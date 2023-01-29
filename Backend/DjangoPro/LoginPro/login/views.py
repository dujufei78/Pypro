from django.shortcuts import render, redirect

# Create your views here.
from login import models
from login.form import UserForms
from login.models import User


def index(request):
    '''
    首页
    :param request:
    :return:
    '''
    return render(request, 'login/index.html')


def login(request):
    '''
    登陆
    :param request:
    :return:
    '''
    # 第一种写法，不使用forms的原生写法
    # if request.method == "POST":
    #     username = request.POST.get("username")
    #     password = request.POST.get("password")
    #     message = "用户名和密码必须都得填写"
    #     if username and password:
    #         username = username.strip()
    #         try:
    #             userobj = User.objects.get(name=username)
    #             if userobj.password == password:
    #                 return redirect('/index/')
    #             else:
    #                 message = "密码错误"
    #         except Exception as e:
    #             message = '用户名不存在'
    #
    #     return render(request, 'login/login.html', {"message": message})
    # return render(request, 'login/login.html')

    # 第二种，使用forms的写法
    if request.method == "POST":
        login_form = UserForms(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    return redirect('/index/')
                else:
                    message = "密码不正确，请重新输入"
            except Exception as e:
                message = "用户不存在"
        return render(request, 'login/login.html', locals())
    login_form = UserForms()
    return render(request, 'login/login.html', locals())


def register(request):
    '''
    注册
    :param request:
    :return:
    '''
    return render(request, 'login/register.html')


def logout(request):
    '''
    注销
    :param request:
    :return:
    '''
    return redirect('/index')


def test(request):
    '''
    注册
    :param request:
    :return:
    '''
    return render(request, 'login/test.html')
