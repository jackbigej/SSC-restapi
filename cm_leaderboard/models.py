from django.db import models

# Create your models here.

class School(models.Model):
	name = models.CharField(max_length=100, unique=True)
	total_cm = models.IntegerField()
	year_cm = models.IntegerField()
	term_cm = models.IntegerField()
	month_cm = models.IntegerField()
	first_post = models.DateField()

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

