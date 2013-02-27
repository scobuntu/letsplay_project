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

class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	
	verbose_name_plural = "categories"

	def __unicode__(self):
		return self.name

# Create your models here.
class Game(models.Model):
	name = models.CharField(max_length=128, unique=True)
	ageLevel = models.CharField(max_length=128, choices=AGE_LEVEL_CHOICES)
	sex = models.CharField(max_length=128, choices=GENDER)
	category = models.ForeignKey('Category')
	embedCode = models.TextField()
	screenShot = models.FileField(upload_to='static/game/thumbnails', blank=True)
        
        def __unicode__(self):
                return self.name

class Video(models.Model):
	name = models.CharField(max_length=128, unique=True)
	ageLevel = models.CharField(max_length=128, choices=AGE_LEVEL_CHOICES)
	sex = models.CharField(max_length=128, choices=GENDER)
	category = models.ForeignKey('Category')
	embedCode = models.TextField()
	screenShot = models.FileField(upload_to='static/video/thumbnails', blank=True)
        
        def __unicode__(self):
                return self.name
                
class Background(models.Model):
	name = models.CharField(max_length=128, unique=True)
	ageLevel = models.CharField(max_length=128, choices=AGE_LEVEL_CHOICES)
	sex = models.CharField(max_length=128, choices=GENDER)
	category = models.ForeignKey('Category')
	screenShot = models.FileField(upload_to='static/backgrounds', blank=True)
        
        def __unicode__(self):
                return self.name
                
class Avatar(models.Model):
	name = models.CharField(max_length=128, unique=True)
	ageLevel = models.CharField(max_length=128, choices=AGE_LEVEL_CHOICES)
	sex = models.CharField(max_length=128, choices=GENDER)
	category = models.ForeignKey('Category')
	embedCode = models.TextField()
	screenShot = models.FileField(upload_to='static/avatar/thumbnails', blank=True)
        
        def __unicode__(self):
                return self.name
    
                
