# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    group = models.IntegerField(blank=True,null=True)

    def __unicode__(self):
        return self.name

class Coach(models.Model):
    name = models.CharField(max_length=30)
    group = models.IntegerField(blank=True,null=True)

    def __unicode__(self):
        return self.name

class duty(models.Model):
    class_1 = models.IntegerField(default=2)
    class_2 = models.IntegerField(default=2)
    class_3 = models.IntegerField(default=2)
    class_4 = models.IntegerField(default=2)
    day_off = models.IntegerField(default=0)

class booking(models.Model):
    group = models.IntegerField(blank=True,null=True)
    person = models.IntegerField(default=0)
    coach  = models.IntegerField(default=0)
    class_time = models.IntegerField(default=0)

class bus_list(models.Model):
    route = models.IntegerField(blank=True,null=True)