from django.db import models

from django.conf import settings


# Create your models here.

class User(models.Model):
    UserName = models.CharField(max_length=35)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=300)
    
    def __str__(self):
        return self.UserName
    

class Todomodel(models.Model):
    user = models.ForeignKey(User, default=1,on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    contents = models.CharField(max_length=50)
    

    def __str__(self):
        return self.title
    


