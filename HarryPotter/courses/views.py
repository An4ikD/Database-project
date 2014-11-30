from django.shortcuts import render
from my_profile.views import *
from HarryPotter.settings import cnx, cursor
from django.http import HttpResponse

# void or int function in C++
def get_courses(request, template_name):
	params = {}

	userID = request.user.id
	userType = get_userType(userID)
	params['profile'] = get_profile(userType, userID)

	if userType == 1:
		params['is_staff'] = True
	else:
		params['is_staff'] = False

	query = ("SELECT ID, name FROM subject ")

	cursor.execute(query)

	temp = []
	for ID, name in cursor:
		t = {}
		t['ID'] = ID
		t['name'] = name

		if userType == 2:
			query = ("SELECT subjectID, studentID FROM study "
					"WHERE subjectID like %s "
					"and studentID like %s" % (ID, userID))
			print query
			cursor.execute(query)

			for subjectID, studentID in cursor:
				if subjectID == None:
					t['status'] = False
				else:
					t['status'] = True

		temp.append(t)

	params['courses'] = temp

	return render(request, template_name, params)

def register_course(request, id, template_name):
	params = {}
	
	userID = request.user.id

	query = ("INSERT INTO study "
                    "(subjectID, studentID) "
                    "VALUES (%s, %s)" % (id, request.user.id))
	cursor.execute(query)
	cnx.commit()

	print query

	params['message'] = "You have successfully registered for this course"

	return render(request, template_name, params)

def drop_course(request, id, template_name):
	params = {}
	
	userID = request.user.id

	query = ("DELETE FROM study "
                    "where subjectID like %s "
                    "and studentID like %s" % (id, request.user.id))

	cursor.execute(query)
	cnx.commit()

	print query

	params['message'] = "You have successfully dropped this course"

	return render(request, template_name, params)