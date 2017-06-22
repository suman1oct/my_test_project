
# django imports
from django.db import models

#local imports
from .choices import PACKAGE_CHOICES



class UserProfile(models.Model):
	name = models.CharField(max_length = 100, null = False)
	email = models.EmailField()
	password = models.CharField(max_length=100)


