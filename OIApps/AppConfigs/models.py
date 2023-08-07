from django.db import models
from django.contrib.auth.models import User,Group
import datetime 
import time
# Create your models here.
   
class Category(models.Model):
    name = models.CharField(max_length=100, blank=True, default='NP')
    DataCategory = models.CharField(max_length=100, blank=False, default='PULL')
    ResponseData= models.TextField(blank=False, default='Response')
    CreatedByUser= models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    UdatedTime = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return (self.name)
class App(models.Model):
    name = models.CharField(max_length=100, blank=True,unique=True, default='OI Test APP')
    AppID = models.CharField(max_length=100, blank=False, default='PULL')
    Group= models.ForeignKey(Group, blank=True, null=True, on_delete=models.CASCADE)
    Category= models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
    CreatedByUser= models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.name 
    
class Scope(models.Model):
    name = models.CharField(max_length=100, blank=True, default='TestSecret')
    Tag = models.CharField(max_length=100, blank=True, default='TestTag')
    Type= models.CharField(max_length=100, blank=True, default='TestTag')
  
    CreatedByUser= models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return (self.name)
