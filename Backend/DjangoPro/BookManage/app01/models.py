from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Book(models.Model):
    nid = models.AutoField(primary_key=True)  # 自增id(可以不写，默认会有自增id)
    title = models.CharField(max_length=32)
    publishDdata = models.DateField()  # 出版日期
    price = models.DecimalField(max_digits=5, decimal_places=2)  # 一共5位，保留两位小数

    # 一个出版社有多本书，关联字段要写在多的一方
    # 不用命名为publish_id，因为django为我们自动就加上了_id
    publish = models.ForeignKey("Publish", on_delete=models.CASCADE)  # foreignkey（表名）建立的一对多关系
    # publish是实例对象关联的出版社对象
    authorlist = models.ManyToManyField("Author")  # 建立的多对多的关系

    def __str__(self):
        return self.title


class Publish(models.Model):
    # 不写id的时候数据库会自动给你增加自增id
    name = models.CharField(max_length=32)
    addr = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class AuthorDeital(models.Model):
    tel = models.IntegerField()
    addr = models.CharField(max_length=32)
    author = models.OneToOneField("Author", on_delete=models.CASCADE)  # 建立的一对一的关系


class UserInfo(models.Model):
    gender = (
        ("male", "男"),
        ("female", "女")
    )
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default="男")
    c_time = models.DateTimeField(auto_now_add=True)

    # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
    #                              message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    #
    # ph = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list

    def __str__(self):
        return self.username

    class Meta:
        ordering = ["c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"
