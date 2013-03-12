from django.db import models

AGE_LEVEL_CHOICES = (
	('All', 'All'),
	('0-2', 'nursery'),
	('3-4','preschool'),
	('5-7','primary'),
	('8-10','primary2'),
	)

GENDER = (
	('No preference', 'No preference'),
	('Male', 'Boy'),
	('Female','Girl'),
	)

TYPES = (
	('Game', 'Game'),
	('Video', 'Video'),
	)

class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	
	class Meta:
		verbose_name_plural = "categories"

	def __unicode__(self):
		return self.name


class AgeGroup(models.Model):
	
	age = models.CharField(max_length=128)

	def __unicode__(self):
		return self.age

class Content(models.Model):
	content_type = models.CharField(max_length=128, choices=TYPES)
	name = models.CharField(max_length=128, unique=True)
	ageGroup = models.ForeignKey(AgeGroup)
	sex = models.CharField(max_length=128, choices=GENDER)
	category = models.ManyToManyField('Category')
	embedCode = models.TextField()
	screenShot = models.FileField(upload_to='static/content/thumbnails', blank=True)
	audio = models.FileField(upload_to='static/content/sounds', blank=True)
	
	def __unicode__(self):
		return self.name
	
                
class Background(models.Model):
	name = models.CharField(max_length=128, unique=True)
	screenShot = models.FileField(upload_to='static/backgrounds', blank=True)

	def __unicode__(self):
		return self.name
                
class Avatar(models.Model):
	name = models.CharField(max_length=128, unique=True)
	embedCode = models.TextField()
	screenShot = models.FileField(upload_to='static/avatar/thumbnails', blank=True)

	def __unicode__(self):
		return self.name
    
                
