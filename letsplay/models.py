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

# Create your models here.
class Game(models.Model):
	#primary key id will be assigned by django?
	name = models.CharField(max_length=128, unique=True)
	ageLevel = models.CharField(max_length=128, choices=AGE_LEVEL_CHOICES)
	sex = models.CharField(max_length=128, choices=GENDER)
	category = models.CharField(max_length=128)
	embedCode = models.TextField()
	screenShot = models.FileField(upload_to='static/game/thumbnails', blank=True)
        
        def __unicode__(self):
                return self.name

class Video(models.Model):
	#primary key id will be assigned by django?
	name = models.CharField(max_length=128, unique=True)
	ageLevel = models.CharField(max_length=128, choices=AGE_LEVEL_CHOICES)
	sex = models.CharField(max_length=128, choices=GENDER)
	category = models.CharField(max_length=128)
	embedCode = models.TextField()
	screenShot = models.FileField(upload_to='static/video/thumbnails', blank=True)
        
        def __unicode__(self):
                return self.name
                
class Background(models.Model):
	#primary key id will be assigned by django?
	name = models.CharField(max_length=128, unique=True)
	ageLevel = models.CharField(max_length=128, choices=AGE_LEVEL_CHOICES)
	sex = models.CharField(max_length=128, choices=GENDER)
	category = models.CharField(max_length=128)
	screenShot = models.FileField(upload_to='static/backgrounds', blank=True)
        
        def __unicode__(self):
                return self.name
                
class Avatar(models.Model):
	#primary key id will be assigned by django?
	name = models.CharField(max_length=128, unique=True)
	ageLevel = models.CharField(max_length=128, choices=AGE_LEVEL_CHOICES)
	sex = models.CharField(max_length=128, choices=GENDER)
	category = models.CharField(max_length=128)
	embedCode = models.TextField()
	screenShot = models.FileField(upload_to='static/avatar/thumbnails', blank=True)
        
        def __unicode__(self):
                return self.name
    
                
