from hashlib import blake2b
from random import choices
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models
from accounts.models import User
# Create your models here.


priority = [
    (1, "High priority"),
    (2, "medium priority"),
    (3, "low priority"),
    
]

class work_space_tag(models.Model):
    tag_name=models.CharField(max_length=255)
    def __str__(self):
        return self.tag_name

class work_space(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='workspace')
    title=models.CharField(max_length=255,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    category=models.CharField(max_length=255,null=True,blank=True)
    tags=models.ManyToManyField(work_space_tag,related_name='workspace_tag')
    def __str__(self):
        return self.title




class project(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='workspace_project')
    title=models.CharField(max_length=255)
    description=models.TextField()
    project_category=models.CharField(max_length=255)
    open_positions=models.CharField(max_length=255)
    start_date=models.DateField()
    due_Date=models.DateField()
    estimated_budget=models.CharField(max_length=255)




class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='workspace_task')
    name=models.CharField(max_length=255)
    description=models.TextField()
    start_date=models.DateField()
    due_Date=models.DateField()
    priority=models.IntegerField(choices=priority,null=True,blank=True)

