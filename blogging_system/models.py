from django.db import models
from django.utils import timezone


class Post(models.Model):
	  title = models.CharField(max_length=200)
	  text = models.TextField()
	  created_at = models.DateTimeField(default=timezone.now)
	  published_at = models.DateTimeField(blank=True, null=True)

	  def __str__(self):
	  	  return self.title

	  def publish(self):
	  	  self.published_at = timezone.now()
	  	  self.save
