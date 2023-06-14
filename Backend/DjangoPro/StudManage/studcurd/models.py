from django.db import models


# Create your models here.
class UserInfo(models.Model):
    """
    用户表:既有班主任也有老师
    """
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    email = models.EmailField(max_length=32)
    ut = models.ForeignKey(to="UserType", on_delete=models.CASCADE)  # 用户和用户类型一对多的关系
    teacher_classes = models.ManyToManyField(to="Classes")  # 老师和班级的多对多关系

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'


class UserType(models.Model):
    """
    用户类型表
    """
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '用户类型'
        verbose_name_plural = '用户类型'


class Classes(models.Model):
    """
    班级表
    """
    name = models.CharField(max_length=32)
    classteacher = models.ForeignKey(to="UserInfo", on_delete=models.CASCADE)  # 班级和班主任是一对多的关系

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '班级表'
        verbose_name_plural = '班级表'


class Student(models.Model):
    """
    学生表
    """
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    cls = models.ForeignKey(to="Classes", on_delete=models.CASCADE)  # 学生和班级的一对多关系

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '学生表'
        verbose_name_plural = '学生表'
