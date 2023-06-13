from django.contrib.auth.backends import ModelBackend
from django.shortcuts import render

# Create your views here.
class CustonBackend(ModelBackend):
    '''
    自定义用户认证
    '''
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            # 用户名和收集都能登陆
            user = User.objects.get(
                Q(username=username) | Q(mobile=username)
            )
            if user.check_password(password):
                return user
        except Exception as e:
            return None
