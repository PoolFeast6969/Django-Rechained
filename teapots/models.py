from django.db import models
from django.conf import settings

class Card(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	date_created = models.DateTimeField('date created', auto_now_add=True)
	uses = models.IntegerField(default=0)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.content
	class Meta:
		abstract = True

class Question(Card):
	content = models.CharField(max_length=150)

class Answer(Card):
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='owner')
	content = models.CharField(max_length=50)

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email_valid = models.BooleanField('email verified', default=False)
