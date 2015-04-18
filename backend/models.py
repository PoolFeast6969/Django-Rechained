from django.db import models
from django.contrib.auth.models import *

class Card(models.Model):
	author = models.ForeignKey(User)
	date_created = models.DateTimeField('date created')
	uses = models.IntegerField(default=0)
	votes = models.IntegerField(default=0)
	class Meta:
		abstract = True
	def __str__(self):
		return self.content

class Question(Card):
	content = models.CharField(max_length=150)

class Answer(Card):
	owner = models.ForeignKey(User, related_name='owner')
	content = models.CharField(max_length=50)
