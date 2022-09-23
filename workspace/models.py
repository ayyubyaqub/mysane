from hashlib import blake2b
from unicodedata import category
from django.db import models
from accounts.models import User
# Create your models here.


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