from django.shortcuts import render, redirect

# Create your views here.
from studcurd import models
from studcurd.forms import LoginForm


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            user = models.Userinfo.objects.filter(*form.cleaned_data).first()
            if user:
                request.session['user_info'] = {'id': user.id, 'username': user.username}
                return redirect('/teacherindex/')
            else:
                form.add_error('password', '用户名或者密码不正确')
    return render(request, 'login.html', locals())
