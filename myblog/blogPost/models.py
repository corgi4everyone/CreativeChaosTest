from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    title_tag = models.CharField(max_length=100)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    catagory= models.ManyToManyField('Catagory',blank=True)
    body = models.TextField(blank=True,null=True)
    id  = models.UUIDField(default=uuid.uuid4, null=False, unique=True, primary_key=True, editable=False)
    created_at= models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title

class Catagory(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
