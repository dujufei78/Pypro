# -*- encoding: utf-8 -*-
## 大纲

## 创建一个类
## 对象之前的交互
## 继承
## 组合
# 继承的方式
# 组合的方式
# 私有属性
## 方法
# 静态方法
# 类方法
# 属性方法
## 多态
## 类的特殊方法

## 创建一个类
# class Car:
#     def __init__(self, type, price):
#         self.type = type
#         self.price = price
#
#     def carinfo(self):
#         print('the cars type is %s, and price is %s' % (self.type, self.price))
#
# tesla = Car('tesla', 200)
# tesla.carinfo()

## 对象之前的交互
# class HouYi:
#     '''
#     王者荣耀格斗实现-后裔干孙悟空
#     '''
#     camp = 'Demacia'
#
#     def __init__(self, name, life_value=100, arrressive=50):
#         self.name = name
#         self.life_value = life_value
#         self.arrressive = arrressive
#
#     def attack(self, enemy):
#         enemy.life_value -= self.arrressive
#
#
# class SunWuKong:
#     '''
#     王者荣耀格斗实现-后裔干孙悟空
#     '''
#
#     def __init__(self, name, life_value=200, arrressive=40):
#         self.name = name
#         self.life_value = life_value
#         self.arrressive = arrressive
#
#     def attack(self, enemy):
#         enemy.life_value -= self.arrressive
#
#
# houyi = HouYi('后裔')
# sunwukong = SunWuKong('孙悟空')
#
# print(houyi.life_value)
# houyi.attack(sunwukong)
# print(sunwukong.life_value)

## 继承
# 继承的目的：解决代码重用问题
# 父类(基类)、子类(派生类)
# class People:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         print('%s is eating......' % self.name)
#
#     def talk(self):
#         print('%s is talking......' % self.name)
#
#     def sleep(self):
#         print('%s is sleeping......' % self.name)
#
#
# class Man(People):
#     def __init__(self, name, age, money):
#         super(Man, self).__init__(name, age)
#         self.money = money
#
#     def standing_pee(self):
#         print('%s is standing pee......' % self.name)
#
#
# class Woman(People):
#     def __init__(self, name, age):
#         super(Woman, self).__init__(name, age)
#
#     def pregnant(self, baby_name):
#         print('%s is pregnant,the baby is %s......' % (self.name, baby_name))
#
#
# m1 = Man('杨师', 27, 12000)
# m1.standing_pee()
#
# w1 = Woman('无敌', 22)
# w1.pregnant('小杨师')


## 组合
# 继承：当类之间有很多相似的功能，提取出来，做成基类，代码比较简洁
# 组合：继承是一种"是"的关系，男人是人；而组合是一种"有"的关系，后裔有装备

# 组合的例子：
# class Equip():
#     def shoot(self):
#         print('shoot an arrow....')
#
#
# class Houyi():
#     def __init__(self, name):
#         self.name = name
#         self.equip = Equip()  # 用Equip产生一个装备给实例
#
#
# houyi = Houyi('后裔')
# houyi.equip.shoot()


# 继承与组合例子：
# class People(object):
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#
# class Teacher(People):
#     def __init__(self, name, age, sex, job):
#         super(Teacher, self).__init__(name, age, sex)
#         self.job = job
#         self.course = []
#         self.students = []
#
#
# class Student(People):
#     def __init__(self, name, age, sex):
#         super(Student, self).__init__(name, age, sex)
#         self.course = []
#
#
# class Course(object):
#     def __init__(self, name, perid, price):
#         self.name = name
#         self.perid = perid
#         self.price = price
#
#     def course_info(self):
#         print('%s %s %s' % (self.name, self.perid, self.price))
#
#
# # 老师和学生对象
# jack = Teacher('cui xiao zhen', 37, 'male', 'teacher')
# dj = Student('dj', 22, 'male')
#
# # 课程
# python = Course('python', '8months', 19800)
# linux = Course('linux', '5months', 10000)
#
# # 为老师添加课程，为学生添加课程
# jack.course.append(python)
# jack.course.append(linux)
#
# dj.course.append(python)
#
# # 为老师添加学生
# jack.students.append(dj)
#
# # 使用
# print(jack.course)
# for i in jack.course:
#     i.course_info()

# 私有属性
# class People:
#     def __init__(self, name, age):
#         # 属性加 __ ,隐藏属性，不让外部访问
#         self.__name = name
#         self.__age = age
#
#     def eat(self):
#         print('%s %s' % (self.name, self.age))
#
#
# jack = People('jack', 33)
# jack.eat()


## 方法
# 静态方法 @staticmethod
# 类方法 @classmethod
# 属性方法 #property


# 若我们要实现一个学生的类 ，里面要实现3功能，分别是：
# 功能1：计算每个学生的总成绩 ，即get_total_score()方法
# 功能2 ：对实例化的学生进行总成绩排名 ，即rank()方法
# 功能3：对考试时间说明 ，即exam_time()方法
# import random
#
#
# class Students(object):
#     scores = []
#
#     def __init__(self, name):
#         self.name = name
#
#     # 实例方法：
#     # 计算每个学生的总成绩是针对的每个学生 ，因此实例化不同的学生，从而显示它的总成绩 ，所以定义实例方法是合理的
#     def get_total_score(self):  # 返回某位学生的总成绩
#         total_score = random.randint(200, 600)
#         student_scores = (self.name, total_score)
#         Students.scores.append(student_scores)
#         return student_scores
#
#     # 类方法
#     # 对实例化的学生进行总成绩排名，这个排名很明显是对这个对象的整体(类)进行的排名 ，通过实例化学生(对象)调用排名很明显是不合理的，而应该对整个学生，即学生的这个类进行排名 ，故它定义成类方法是合理的
#     @classmethod
#     def rank(cls):  # 学生成绩排名
#         total_scores = Students.scores
#         return sorted(total_scores, key=lambda x: x[1], reverse=True)
#
#     # 静态方法
#     # 静态方法其实和类没什么关系了，仅仅托管于某个类的名称空间中，便于维护使用。静态方法不可以访问实例变量或类变量
#     # 对考试时间说明 ，这个功能即用于学生 ，但是它又是独立于学生，在这个方法中并不会用到类或实例中的属性和方法 。故它申明成静态方法是比较合理的
#     @staticmethod
#     def exam_time():  # 考试时间说明
#         return {"考试时间": '上午10~12点，下午2~4点'}
#
#     # 属性方法
#     # desc变成了属性，而不是方法了，无需括号调用
#     @property
#     def desc(self):
#         return '每个学生不能作弊'
#
#
# a = Students('张三')
# a.get_total_score()  # 1.实例方法调用：通过实例对象来调用
# print(a.get_total_score())
# b = Students('李四')
# b.get_total_score()
# c = Students('王五')
# c.get_total_score()
# d = Students('赵六')
# d.get_total_score()
# e = Students('刘七')
# e.get_total_score()
#
# print(Students.rank())  # 2.类方法调用：使用类名调用，也可以使用实例对象调用
# # print(Students('小王').rank())
#
# print(Students.exam_time())  # 3.静态方法调用：使用类名调用，也可以使用实例对象调用
# # print(Students('').exam_time())
#
# print(Students('').desc)  # 4.属性方法调用：实例对象调用



