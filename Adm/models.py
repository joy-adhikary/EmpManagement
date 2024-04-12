from django.db import models
from Emp.models import Emp
# Create your models here

class Admin(models.Model):
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=32)
    email = models.EmailField()
    user_type = models.CharField(max_length=20)
    # foreignKey te always full model ke define korty hoi. 
    emp = models.ForeignKey(Emp, on_delete=models.CASCADE, related_name='emp', blank=True, null=True)

    
    def __str__(self):
        return self.user_name