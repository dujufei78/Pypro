from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.
@login_required
def dashboard(request):
    return render(request,'crm/dashboard.html')

def acc_login(request):
    error_message = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 验证
        user= authenticate(username=username, password=password)
        if user:
            login(request, user)
            # 如果next有值，就获取next的值，没有就跳转到首页
            return redirect(request.GET.get('next', '/crm'))
        else:
            error_message = '用户名或者密码错误'
    return render(request, 'login.html', locals())
def acc_logout(request):
    return redirect('/login/')
