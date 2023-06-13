#-*- encoding: utf-8 -*-
# -*- coding:utf-8 -*-
from django.test import TestCase

# Create your tests here.
import pymysql

db = pymysql.connect(host="182.44.2.116", user="root", password="Zp920604...", database="bisontest")
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Database version : %s " % data)
