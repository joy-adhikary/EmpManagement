from django.db import models

# Create your models here.

class Admin(models.Model):
    username = models.CharField(max_length=50),
    password = models.CharField(max_length=32),
    email = models.EmailField(),
    user_type = models.CharField(max_length=20, default='')
    
    # def __str__(self):
    #     return self.username,self.user_type