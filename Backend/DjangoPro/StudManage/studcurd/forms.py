# -*- encoding: utf-8 -*-
from django.shortcuts import render, redirect, HttpResponse
from studcurd import models
# Create your views here.
from django.forms import Form
from django.forms import fields
from django.forms import widgets
from django.conf import settings
from django.core.validators import ValidationError
from django.core.validators import RegexValidator


# 1、创建规则
class TeacherForm(Form):  # 必须继承Form
    # 创建字段，本质上是正则表达式
    username = fields.CharField(
        required=True,  # 必填字段
        error_messages={"required": "用户名不能为空！！"},  # 显示中文错误提示
        widget=widgets.TextInput(attrs={"placeholder": "用户名", "class": "form-control"}),  # 自动生成input框
        label="姓名",
        label_suffix=":"
    )
    password = fields.CharField(required=True, error_messages={'required': '密码不能为空'},
                                widget=widgets.PasswordInput(attrs={'placeholder': '密码', 'class': 'form-control'}),
                                label="密码",
                                label_suffix=":"
                                )  # 不能为空

    email = fields.EmailField(
        required=True,
        error_messages={"required": "邮箱不能为空！！", "invalid": "无效的邮箱"},
        widget=widgets.EmailInput(attrs={"placeholder": "邮箱", "class": "form-control"}),  # 自动生成input框
        label="邮箱",
        label_suffix=":"
    )  # 不能为空且邮箱格式要一致
    teacher_classes = fields.MultipleChoiceField(
        label="任教班级",
        label_suffix=":",
        choices=[]  # 注意一定要用values_list

    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["teacher_classes"].choices = models.Classes.objects.values_list("id", "name")

    def clean_name(self):
        name = self.cleaned_data["name"]
        valid = models.Student.objects.filter(name=name).first()
        if valid:
            raise ValidationError("用户名已存在")
        return name


class LoginForm(Form):
    username = fields.CharField(
        required=True,  # 必填字段
        min_length=3,
        max_length=16,
        error_messages={
            "required": "用户名不能为空",
            "min_length": "长度不能小于3",
            "max_length": "长度不能大于16"
        },
        widget=widgets.TextInput({"placeholder": "username", "class": "form-control"})
    )
    password = fields.CharField(
        required=True,
        min_length=3,
        max_length=16,
        error_messages={
            "required": "密码不能为空",
            "min_length": "密码长度不能小于3",
            "max_length": "密码长度不能大于16",
            # "invalid":"密码格式错误"
            # error_messages的优先级高，如果写上"invalid":"密码格式错误"这个就会优先显示这个错误
        },
        widget=widgets.PasswordInput({"placeholder": "password", "class": "form-control"}),
        validators=[RegexValidator("\d+", "密码只能是数字")]  # 可以进行正则匹配提示错误
    )

    def clean_username(self):
        user = self.cleaned_data["username"]
        is_exits = models.UserInfo.objects.filter(username=user).count()
        if not is_exits:
            raise ValidationError("用户名和密码错误")
        return user  # 必须有return


class StudentForm(Form):  # 必须继承Form
    # 创建字段，本质上是正则表达式

    name = fields.CharField(
        required=True,  # 必填字段
        error_messages={"required": "姓名不能为空！！"},  # 显示中文错误提示
        widget=widgets.TextInput(attrs={"placeholder": "姓名", "class": "form-control"}),  # 自动生成input框
    )
    age = fields.CharField(required=True, error_messages={'required': '年龄不能为空'},
                           widget=widgets.TextInput(attrs={'placeholder': '年龄', 'class': 'form-control'}),
                           )  # 不能为空
    class_list = models.Classes.objects.all().values_list('id', "name")
    cls_id = fields.ChoiceField(choices=class_list)

    # 这个方法判断用户名存在不
    def clean_name(self):
        name = self.cleaned_data["name"]  # 只能拿自己当前的字段值
        valid = models.Student.objects.filter(name=name).first()
        if valid:
            raise ValidationError("用户名已存在")  # 主动报错
        return name  # 必须有返回值


class ClassesForm(Form):
    name = fields.CharField(
        required=True,  # 必填字段
        error_messages={"required": "姓名不能为空！！"},  # 显示中文错误提示
        widget=widgets.TextInput(attrs={"placeholder": "姓名", "class": "form-control"}),  # 自动生成input框
    )
    # 如果直接定义成classteacher_id，，_id 的形式，这样你添加数据的时候不会时时更新，所以在下面定义一个重写的方法
    # classteacher_id = fields.ChoiceField(choices= models.UserInfo.objects.filter(ut_id = settings.ROLE_CLASSTEACHER).values_list('id', "username"))

    classteacher_id = fields.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):  # 重写init方法，时时更新
        super().__init__(*args, **kwargs)
        self.fields["classteacher_id"].choices = models.UserInfo.objects.filter(
            ut_id=settings.ROLE_CLASSTEACHER).values_list('id', "username")
