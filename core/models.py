from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.OneToOneField(User)
	about = models.CharField(max_length=140, blank=True)
	dob = models.DateField(blank=True)
	
	def __str__(self):
		return str(self.user)

