from django.db import models
from django.contrib.auth.models import User


class Tweet(models.Model):
	text = models.CharField(max_length=280, blank=False)
	user = models.ForeignKey(User)
	timestamp = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)
	retweets = models.IntegerField(default=0)

	def __str__(self):
		return str(self.user)