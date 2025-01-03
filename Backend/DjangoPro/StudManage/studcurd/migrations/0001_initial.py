# Generated by Django 4.0.10 on 2023-03-06 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name': '班级表',
                'verbose_name_plural': '班级表',
            },
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name': '用户类型',
                'verbose_name_plural': '用户类型',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=32)),
                ('teacher_classes', models.ManyToManyField(to='studcurd.classes')),
                ('ut', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studcurd.usertype')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField()),
                ('cls', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studcurd.classes')),
            ],
            options={
                'verbose_name': '学生表',
                'verbose_name_plural': '学生表',
            },
        ),
        migrations.AddField(
            model_name='classes',
            name='classteacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studcurd.userinfo'),
        ),
    ]
