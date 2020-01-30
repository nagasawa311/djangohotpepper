from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class List(models.Model):
	item_id=models.CharField(max_length=10)
	def __str__(self):
		return self.item_id