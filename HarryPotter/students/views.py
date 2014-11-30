from django.shortcuts import render
from my_profile.views import *
from HarryPotter.settings import cnx, cursor

def get_students(request, template_name):
	params = {}

	userID = request.user.id
	userType = get_userType(userID)

	if userType == 1:
		params['is_staff'] = True
	else:
		params['is_staff'] = False
		
	params['profile'] = get_profile(userType, userID)

	query = ("SELECT userID, name, surname FROM student ")

	cursor.execute(query)

	temp = []
	for userID, name, surname in cursor:
		if userID != request.user.id:
			t = {}
			t['userID'] = userID
			t['name'] = name
			t['surname'] = surname
			temp.append(t)

	params['students'] = temp

	return render(request, template_name, params)

def dismiss_student(request, id, template_name):
	params = {}
	
	userID = request.user.id

	query = ("DELETE FROM study "
			"where studentID like %s" % (id))
	cursor.execute(query)
	cnx.commit()

	query = ("DELETE FROM student "
            "where userID like %s" % (id))
	cursor.execute(query)
	cnx.commit()

	params['message'] = "You have successfully dismissed this student!"

	return render(request, template_name, params)


