# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(name=u"name", max_length=100, blank=True)
    money = models.IntegerField(default=0)
