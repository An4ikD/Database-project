from django.shortcuts import render
from my_profile.views import *
from HarryPotter.settings import cnx, cursor

def get_staff(request, template_name):
	params = {}

	userID = request.user.id
	userType = get_userType(userID)

	if userType == 1:
		params['is_staff'] = True
	else:
		params['is_staff'] = False
	params['profile'] = get_profile(userType, userID)

	query = ("SELECT userID, name, surname FROM staff ")

	cursor.execute(query)

	temp = []
	for userID, name, surname in cursor:
		if userID != request.user.id:
			t = {}
			t['userID'] = userID
			t['name'] = name
			t['surname'] = surname
			temp.append(t)

	params['staffs'] = temp

	return render(request, template_name, params)

def dismiss_staff(request, id, template_name):
	params = {}
	
	userID = request.user.id

	query = ("UPDATE subject "
			"set teacherID=NULL "
			"where teacherID like %s" % (id))
	print query
	cursor.execute(query)
	cnx.commit()

	query = ("DELETE FROM staff "
            "where userID like %s" % (id))
	cursor.execute(query)
	cnx.commit()

	params['message'] = "You have successfully dismissed this member of staff!"

	return render(request, template_name, params)
