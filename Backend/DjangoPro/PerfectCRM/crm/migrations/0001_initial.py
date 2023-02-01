# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='校区名', max_length=64, unique=True)),
                ('addr', models.CharField(verbose_name='地址', max_length=128, blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClassList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('class_type', models.SmallIntegerField(verbose_name='班级类型', default=0, choices=[(0, '脱产'), (1, '周末'), (2, '网络班')])),
                ('semester', models.SmallIntegerField(verbose_name='学期')),
                ('start_date', models.DateField(verbose_name='开班日期')),
                ('graduate_date', models.DateField(verbose_name='毕业日期', blank=True, null=True)),
                ('branch', models.ForeignKey(verbose_name='校区', to='crm.Branch')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='课程名称', max_length=64, unique=True)),
                ('price', models.PositiveSmallIntegerField(verbose_name='价格')),
                ('period', models.PositiveSmallIntegerField(verbose_name='课程周期（月）', default=5)),
                ('outline', models.TextField(verbose_name='大纲')),
            ],
        ),
        migrations.CreateModel(
            name='CourseRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('day_num', models.PositiveSmallIntegerField(verbose_name='课程节次')),
                ('title', models.CharField(verbose_name='本节主题', max_length=64)),
                ('content', models.TextField(verbose_name='本节内容')),
                ('has_homework', models.BooleanField(verbose_name='本节有作业', default=True)),
                ('homework', models.TextField(verbose_name='作业需求', blank=True, null=True)),
                ('date', models.DateField(verbose_name='创建的时间', auto_now_add=True)),
                ('class_grade', models.ForeignKey(verbose_name='上课班级', to='crm.ClassList')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerFollowUp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('content', models.TextField(verbose_name='跟踪内容')),
                ('status', models.SmallIntegerField(verbose_name='客户状态', choices=[(0, '近期无报名计划'), (1, '一个月内报名'), (2, '半个月报名'), (3, '已报名')])),
                ('date', models.DateField(verbose_name='创建的时间', auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='姓名', max_length=64, default=None)),
                ('contact_type', models.SmallIntegerField(default=0, choices=[(0, 'qq'), (1, '微信'), (2, '手机')])),
                ('contact', models.CharField(verbose_name='联系方式', max_length=64, unique=True)),
                ('source', models.SmallIntegerField(verbose_name='客户来源', choices=[(0, 'qq群'), (1, '51CTO'), (2, '百度推广'), (3, '知乎'), (4, '转介绍'), (5, '其它')])),
                ('consult_content', models.TextField(verbose_name='咨询内容')),
                ('status', models.SmallIntegerField(verbose_name='客户状态', choices=[(0, '未报名'), (1, '已报名'), (2, '已经退学')])),
                ('date', models.DateField(verbose_name='创建的时间', auto_now_add=True)),
                ('consult_courses', models.ManyToManyField(verbose_name='咨询课程', to='crm.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Menus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=64)),
                ('url_type', models.SmallIntegerField(default=0, choices=[(0, 'absolute'), (1, 'dynamic')])),
                ('url_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('menus', models.ManyToManyField(verbose_name='动态菜单', blank=True, to='crm.Menus')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('class_grades', models.ForeignKey(verbose_name='班级', to='crm.ClassList')),
                ('customer', models.ForeignKey(verbose_name='客户', to='crm.CustomerInfo')),
            ],
        ),
        migrations.CreateModel(
            name='StudyRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('score', models.SmallIntegerField(verbose_name='得分', default=0, choices=[(100, 'A+'), (90, 'A'), (85, 'B+'), (80, 'B'), (75, 'B-'), (70, 'C+'), (60, 'C'), (40, 'C-'), (-50, 'D'), (0, 'N/A'), (-100, 'COPY')])),
                ('show_status', models.SmallIntegerField(verbose_name='出勤', default=1, choices=[(0, '缺勤'), (1, '已签到'), (2, '迟到'), (3, '早退')])),
                ('note', models.TextField(verbose_name='成绩备注', blank=True, null=True)),
                ('date', models.DateField(verbose_name='创建的时间', auto_now_add=True)),
                ('course_record', models.ForeignKey(verbose_name='课程', to='crm.CourseRecord')),
                ('student', models.ForeignKey(verbose_name='学生', to='crm.Student')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='姓名', max_length=64)),
                ('role', models.ManyToManyField(blank=True, null=True, to='crm.Role')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='menus',
            unique_together=set([('name', 'url_name')]),
        ),
        migrations.AddField(
            model_name='customerinfo',
            name='consultant',
            field=models.ForeignKey(verbose_name='课程顾问', to='crm.UserProfile'),
        ),
        migrations.AddField(
            model_name='customerinfo',
            name='referral_from',
            field=models.ForeignKey(verbose_name='转介绍', blank=True, null=True, to='crm.CustomerInfo'),
        ),
        migrations.AddField(
            model_name='customerfollowup',
            name='customer',
            field=models.ForeignKey(to='crm.CustomerInfo'),
        ),
        migrations.AddField(
            model_name='customerfollowup',
            name='user',
            field=models.ForeignKey(verbose_name='跟进人', to='crm.UserProfile'),
        ),
        migrations.AddField(
            model_name='courserecord',
            name='teacher',
            field=models.ForeignKey(verbose_name='讲师', to='crm.UserProfile'),
        ),
        migrations.AddField(
            model_name='classlist',
            name='course',
            field=models.ForeignKey(verbose_name='课程', to='crm.Course'),
        ),
        migrations.AddField(
            model_name='classlist',
            name='teachers',
            field=models.ManyToManyField(verbose_name='讲师', to='crm.UserProfile'),
        ),
        migrations.AlterUniqueTogether(
            name='courserecord',
            unique_together=set([('class_grade', 'day_num')]),
        ),
        migrations.AlterUniqueTogether(
            name='classlist',
            unique_together=set([('branch', 'class_type', 'course', 'semester')]),
        ),
    ]
