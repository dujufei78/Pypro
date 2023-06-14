from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from app01 import models
from app01.form import UserForms, RegisterForms
from app01.models import UserInfo, Book


# @login_required
def index(request):
    return render(request, 'login/index.html')


def login(request):
    print('----')
    if request.session.get('is_login', None):
        return redirect('/book_list/')
    if request.method == "POST":
        print('////')
        login_form = UserForms(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            print(username, password)
            try:
                userobj = UserInfo.objects.get(username=username)
                pwd = userobj.password
                print('===af===')
                print(pwd, password)
                # 此处可以做加密登陆
                if pwd == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = userobj.id
                    request.session['user_name'] = userobj.username

                    return redirect('/book_list/')
                else:
                    message = '密码错误'
            except Exception as e:
                message = '用户不存在'
        return render(request, 'login/login.html', locals())
    login_form = UserForms()
    return render(request, 'login/login.html', locals())


def register(request):
    if request.session.get('is_login'):
        return redirect('/index/')
    if request.method == 'POST':
        register_form = RegisterForms(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            ph = register_form.cleaned_data['ph']
            if password1 != password2:
                message = '两次密码不相同，请重新输入！'
                return render(request, 'login/register.html', locals())
            else:
                user = UserInfo.objects.filter(username=username)
                if user:
                    message = "用户名已存在，请重新输入！"
                    return render(request, 'login/register.html', locals())
                email = UserInfo.objects.filter(email=email)
                if email:
                    message = "该邮箱已被注册，请重新输入！"
                    return render(request, 'login/register.html', locals())
                print('-------afafdafdf----')
                print(username, password1, email, sex)
                # 创建用户,加密 password=hash_code(password1)
                UserInfo.objects.create(
                    username=username, password=password1,
                    email=email,
                    sex=sex,
                )
                return redirect('/login/')
    register_form = RegisterForms()
    return render(request, 'login/register.html', locals())


# @login_required
def logout(request):
    request.session.flush()

    return redirect('/login/')


# @login_required
def book_list(request):
    book_list = models.Book.objects.all()  # book_list打印的是一个对象  先查看所有的书
    paginator = Paginator(book_list, 4)  # 这里的book_list必须是一个集合对象，把所有的书分页，一页有五个
    print(paginator.page_range)  # range(1, 4)
    page_range = paginator.page_range
    num = request.GET.get("page", 2)  # 得到页数范围,默认有1页
    print(num, type(num))
    book_list = paginator.page(num)  # 显示第一页的内容
    return render(request, "book/booklist.html", {"book_list": book_list, "page_range": page_range, "num": int(num)})


# @login_required
def book_add(request):
    if request.method == 'POST':
        title = request.POST.get("bookname")
        publishDdata = request.POST.get("data")
        author = request.POST.getlist("author")
        price = request.POST.get("price")
        publish = int(request.POST.get("publish"))

        print(author)
        # 添加书籍，一对多和多对多的情况，都是传参数字，一对多：publish_id = 3 ，多对多：['1','2','3']
        book_obj = Book.objects.create(title=title, publishDdata=publishDdata
                                       , price=price, publish_id=publish)
        book_obj.authorlist.add(*author)
        return redirect('/book_list/')
    else:
        publist = models.Publish.objects.all()
        authorlist = models.Author.objects.all()
        return render(request, 'book/book_add.html', locals())


# @login_required
def book_edit(request):
    if request.method == "POST":
        id = int(request.POST.get('book_input_id'))
        title = request.POST.get("bookname")
        data = request.POST.get("data")
        price = request.POST.get("price")
        publish = int(request.POST.get("publish"))
        author = request.POST.getlist("author")
        models.Book.objects.filter(nid=id).update(title=title, publishDdata=data, price=price, publish_id=publish)

        book_obj = models.Book.objects.filter(nid=id).first()
        book_obj.authorlist.clear()
        book_obj.authorlist.add(*author)

        return redirect('/book_list/')
    else:
        id = int(request.GET.get('book_id'))
        book_obj = models.Book.objects.filter(nid=id).first()
        author_obj = models.Author.objects.all()
        pub_obj = models.Publish.objects.all()

        # 默认选中的
        edit_book_authors = book_obj.authorlist.all().values_list('id')
        print('=1111==')
        print(edit_book_authors)
        l = []
        for i in edit_book_authors:
            l.append(i[0])
        print(l)
        return render(request, 'book/book_edit.html',
                      {'book_obj': book_obj, 'auth_obj': author_obj, 'publ_obj': pub_obj, 'l': l})


# @login_required
def book_del(request, id):
    print('----3-----')
    Book.objects.filter(nid=id).delete()
    return redirect('/book_list/')
