# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class data(models.Model):
	comments= models.CharField(max_length=1000)

	def __str__(self):
		return str(self.pk)

class solution(models.Model):
	solution=models.IntegerField()

	def __str__(self):
		return str(self.pk)

