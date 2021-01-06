from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from cm_leaderboard.serializers import UserSerializer, GroupSerializer, SchoolSerializer
from cm_leaderboard.models import School, ClassMeeting, leaderboard_lib
import pandas as pd
import datetime
import logging

def load_csv():
	df = pd.read_csv(r'/Users/jackbigej/Desktop/Smart School Councils/rest_api/SM-rpi/rest_api/cm_leaderboard/csv_files/school_questions.csv')
	for index, row in df.iterrows():

		if len(row) != 3:
			continue

		school_name = row['School Name']
		date = row['Session Date'].split('/')
		question = row['Question']

		if school_name == "" or school_name == "Coronavirus Daily Debates" or school_name == None:
			continue
		
		if isinstance(school_name, float):
			continue

		school_name = school_name.upper()

		if not School.objects.filter(name=school_name).exists():
			temp_school = School.objects.create(name=school_name, cm_count=0)
			temp_school.save()

		date_field = datetime.date(int(date[2]), int(date[1]), int(date[0]))
		
		temp_school = School.objects.get(name=school_name)
		if not ClassMeeting.objects.filter(school=temp_school, date=date_field, question=question):
			temp_class = ClassMeeting.objects.create(school=temp_school, date=date_field, question=question)
			temp_class.save()

			temp_school = School.objects.get(name=school_name)
			temp_school.cm_count += 1
			temp_school.save()

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class SchoolViewSet(viewsets.ModelViewSet):

	load_csv()
	queryset = School.objects.all()
	serializer_class = SchoolSerializer
	permission_classes = [permissions.IsAuthenticated]


class TopAllTimeViewSet(viewsets.ModelViewSet):
	
	load_csv()
	queryset = leaderboard_lib.evaluate_top(School.objects.all())
	serializer_class = SchoolSerializer
	permission_classes = [permissions.IsAuthenticated]

