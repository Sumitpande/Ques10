from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

TITLE_CHOICES = [
    ('Best Student Award','BSA'),
    ('Best Question Award', 'BQA'),
    ('Best Presentation Award','BPA'),
    ('Best Design Award','BDA'),
    
]

class User(AbstractUser):
    phone=models.CharField(max_length=200,blank=True,null=True)
    location=models.CharField(max_length=200,blank=True,null=True)
    picture=models.ImageField(upload_to='profile/',blank=True,null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


class Award(models.Model):
    class Point(models.IntegerChoices):
        BSA_100 = 100
        BQA_20 = 20
        BPA_80 = 80
        BDA_70 = 70
    user=models.ForeignKey('User',on_delete=models.CASCADE,blank=True,null=True)
    title=models.CharField(max_length=200,choices=TITLE_CHOICES)
    points=models.IntegerField(choices=Point.choices)
    
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


