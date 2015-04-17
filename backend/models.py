from django.db import models
from django.contrib.auth.models import *

class Card(models.Model):
	type = models.CharField(max_length=15)
	author = models.ForeignKey(User)
	date_created = models.DateTimeField('date created')
	content = models.CharField(max_length=150)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.content
