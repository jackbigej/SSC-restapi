from django.db import models

# Create your models here.

class cm_leaderboard(models.Model):
	top_alltime = models.CharField(max_length=1000)

class top_alltime(models.Model):
	first = models.CharField(max_length=100)
	second = models.CharField(max_length=100)
	third = models.CharField(max_length=100)
	fourth = models.CharField(max_length=100)
	fifth = models.CharField(max_length=100)

class School(models.Model):
	name = models.CharField(max_length=100, unique=True)
	cm_count = models.IntegerField()

	def school_sort(self):
		return cm_count

class ClassMeeting(models.Model):
	question = models.CharField(max_length=1000)
	date = models.DateField()
	school = models.ForeignKey(School, on_delete=models.CASCADE)

class leaderboard_lib():
	
	def evaluate_top(schools):
		if len(schools) > 5:
			i = 5
			while i < len(schools) and schools[i].cm_count == schools[4].cm_count:
				i += 1
			return schools[0:i]
		else:
			return schools

