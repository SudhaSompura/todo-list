from django.db import models
from django.utils import timezone

class Task(models.Model):
	todo_text = models.TextField()
	date_added = models.DateTimeField(default=timezone.now)
	task_done = models.BooleanField(default=False)

	def __str__(self):
		return 'Task ' + str(self.id)

class User(models.Model):
	fname = models.CharField(max_length=30)
	lname= models.CharField(max_length=30)
	email = models.EmailField(max_length=60)
	password = models.CharField(max_length=30)