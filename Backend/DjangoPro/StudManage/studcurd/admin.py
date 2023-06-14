from django.contrib import admin

# Register your models here.
from studcurd import models

admin.site.register(models.UserInfo)
admin.site.register(models.UserType)
admin.site.register(models.Student)
admin.site.register(models.Classes)
