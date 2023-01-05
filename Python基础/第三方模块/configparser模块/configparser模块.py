#-*- encoding: utf-8 -*-
# read_ini.py
import configparser

config = configparser.ConfigParser()
config.read('test.ini')

# 1.获取sections
print(config.sections())  # ['section1', 'section2']

# 2.获取某一section下的所有options
print(config.options('section1'))  # ['k1', 'k2', 'user', 'age', 'is_admin', 'salary']

# 3.获取items
print(config.items(
    'section1'))  # [('k1', 'v1'), ('k2', 'v2'), ('user', 'egon'), ('age', '18'), ('is_admin', 'true'), ('salary', '31')]

# 4.获取具体的值
res = config.get('section1', 'user')
print(res)  # egon

res = config.getint('section1', 'age')  # 18
print(res)

res = config.getboolean('section1', 'is_admin')
print(res)  # True

res = config.getfloat('section1', 'salary')
print(res)  # 31.0
