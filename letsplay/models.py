from django.db import models

AGE_LEVEL_CHOICES = (
	('N/A', 'N/A'),
	('0-2', 'nursery'),
	('3-4','preschool'),
	('5-7','primary'),
	('8-10','primary2'),
	)

GENDER = (
	('N/A', 'N/A'),
	('Male', 'Male'),
	('Female','Female'),
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

# Create your models here.


class AgeGroup(models.Model):
	
	ageGroup = models.CharField(max_length=128)

	def __unicode__(self):
		return self.ageGroup

class Content(models.Model):
	content_type = models.CharField(max_length=128, choices=TYPES)
	name = models.CharField(max_length=128, unique=True)
	ageGroup = models.ForeignKey(AgeGroup)
	sex = models.CharField(max_length=128, choices=GENDER)
	category = models.ManyToManyField('Category')
	embedCode = models.TextField()
	screenShot = models.FileField(upload_to='static/content/thumbnails', blank=True)
	
	def __unicode__(self):
		return self.name
	
                
class Background(models.Model):
	name = models.CharField(max_length=128, unique=True)
	ageGroup = models.ForeignKey(AgeGroup)
	sex = models.CharField(max_length=128, choices=GENDER)
	category = models.ForeignKey('Category')
	screenShot = models.FileField(upload_to='static/backgrounds', blank=True)

	def __unicode__(self):
		return self.name
                
class Avatar(models.Model):
	name = models.CharField(max_length=128, unique=True)
	ageGroup = models.ForeignKey(AgeGroup)
	sex = models.CharField(max_length=128, choices=GENDER)
	category = models.ForeignKey('Category')
	embedCode = models.TextField()
	screenShot = models.FileField(upload_to='static/avatar/thumbnails', blank=True)

	def __unicode__(self):
		return self.name
    
                
