from django.shortcuts import render
from my_profile.views import *
from HarryPotter.settings import cnx, cursor

def get_staff(request, template_name):
	params = {}

	userID = request.user.id
	userType = get_userType(userID)
	params['profile'] = get_profile(userType, userID)

	query = ("SELECT userID, name, surname FROM staff ")

	cursor.execute(query)

	temp = []
	for userID, name, surname in cursor:
		t = {}
		t['userID'] = userID
		t['name'] = name
		t['surname'] = surname
		temp.append(t)

	params['staffs'] = temp

	return render(request, template_name, params)