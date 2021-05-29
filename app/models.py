# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    address = models.CharField('Address', max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class spareparts(models.Model):                          # зап.части
    name = models.CharField(max_length=100)              # название
    state = models.BooleanField(max_length=100)          # состояние (новый/нет)
    guarantee = models.BooleanField(max_length=100)      # гарантия (да/нет)
    cost = models.IntegerField(default=0)                # стоимость

class tool(models.Model):                                # инструмент
    name = models.CharField(max_length=100)              # название
    cost = models.IntegerField(default=0)                # стоимость

class consumable(models.Model):                          # расходник
    name = models.CharField(max_length=100)              # название
    cost = models.IntegerField(default=0)                # стоимость
