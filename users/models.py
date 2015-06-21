from django.db import models
from django.contrib.auth.models import *

class User(AbstractUser):
    email_valid = models.BooleanField('email verified', default=False)

