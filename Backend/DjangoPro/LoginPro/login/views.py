import hashlib

from django.shortcuts import render, redirect

# Create your views here.
from login import models
from login.form import UserForms, RegisterForms
from login.models import User

def hash_code(s, salt='mysite'):# 加点盐
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()

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
    if request.session.get('is_login', None):
        return redirect('/index')

    if request.method == "POST":
        login_form = UserForms(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)
                # 加密写法
                # if user.password == hash_code(password):
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
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
    if request.session.get('is_login', None):
        return redirect('/index/')
    if request.method == "POST":
        register_form = RegisterForms(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']

            print('===')
            print(sex)
            if password1 != password2:
                message = '两次密码不相同，请重新输入！'
                return render(request, 'login/register.html', locals())
            else:
                user = User.objects.filter(name=username)
                if user:
                    message = "用户名已存在，请重新输入！"
                    return render(request, 'login/register.html', locals())
                email = User.objects.filter(email=email)
                if email:
                    message = "该邮箱已被注册，请重新输入！"
                    return render(request, 'login/register.html', locals())
                print(password1)
                print(password2)
                print('afdfad')
                # 创建用户,加密 password=hash_code(password1)
                User.objects.create(
                    name=username, password=password1,
                    email=email,
                    sex=sex
                )
                return redirect('/login/')
    register_form = RegisterForms()
    return render(request, 'login/register.html', locals())


def logout(request):
    '''
    注销
    :param request:
    :return:
    '''
    if not request.session.get('is_login', None):
        return redirect('/login')
    request.session.flush()
    return redirect('/index')


def test(request):
    '''
    注册
    :param request:
    :return:
    '''
    return render(request, 'login/test.html')
