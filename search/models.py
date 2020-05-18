from django.conf import settings 
from django.db import models

User = settings.AUTH_USER_MODEL
from django.utils import timezone


class Search(models.Model):
	query = models.CharField(max_length=300)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.query
