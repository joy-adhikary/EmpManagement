
from django.db import models

# Create your models here.

class Emp(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=32)
    email = models.EmailField()
    role = models.CharField(max_length=60)
    user_type = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.username
    

#  jodi model a kono kisu change kori tahole python3 manage.py makemigrations appname dite hbe



# creating another model for linking data from emp to admin 

class LinkEmpWithAdmin(models.Model):
    user_name = models.CharField(max_length=502)
    position = models.CharField(max_length=502,default='')
    salary = models.IntegerField()
    emp_id = models.IntegerField()

    def __str__(self):
        return self.user_name

