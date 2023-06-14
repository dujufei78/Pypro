from django.db import models


# Create your models here.
class UserInfo(models.Model):
    USER_TYPE = (
        (1, '普通用户'),
        (2, 'VIP'),
        (3, 'SVIP')
    )
    user_type = models.CharField(choices=USER_TYPE, max_length=32)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=256)


class UserToken(models.Model):
    user = models.OneToOneField(UserInfo, on_delete=models.CASCADE)
    token = models.CharField(max_length=256)
