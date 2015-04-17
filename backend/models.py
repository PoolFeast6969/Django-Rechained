from django.db import models


class User(models.Model):
        username = models.CharField(max_length=15)
	fullname = models.CharField('full name', max_length=20)
        email = models.CharField(max_length=40)
	date_created = models.DateTimeField('date created')

	def __str__(self):
		return self.username

class Card(models.Model):
	type = models.CharField(max_length=15)
	author = models.ForeignKey(User)
	date_created = models.DateTimeField('date created')
	content = models.CharField(max_length=150)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.content
