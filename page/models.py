from django.db import models

# Create your models here.

class Tag(models.Model):
	name = models.CharField(max_length=50)
	
	def __str__(self):
		return self.name

class Page(models.Model):
	title = models.CharField(max_length=100)
	time = models.TimeField(auto_now=True)	

	#Name of Image
	titleImage = models.CharField(max_length=100)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.title

	#TODO: Change the ID Values so that it looks random in the future	
	
