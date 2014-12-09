from django.shortcuts import render
from my_profile.views import *
from HarryPotter.settings import cnx, cursor
from students.forms import *

def get_students(request, template_name):
	params = {}

	userID = request.user.id
	userType = get_userType(userID)

	if userType == 1:
		params['is_staff'] = True
	else:
		params['is_staff'] = False
		
	params['profile'] = get_profile(userType, userID)

	searchquery = ""

	if request.method == 'POST':
		searchForm = searchStudentForm(request.POST)
		if searchForm.is_valid:
			id = request.POST.get('id')
			name = request.POST.get('name')
			surname = request.POST.get('surname')
			houseName = request.POST.get('houseName')

			if id == "" and name == "" and surname == "" and houseName == "":
				pass
			else:
				searchquery += "WHERE "
				put = False

				if id != "":
					searchquery += "userID like %s " % (id)
					put = True
				if name != "":
					if put:
						searchquery += "AND "
					searchquery += "name like %s " % ('"' + name + '"')
					put = True
				if surname != "":
					if put:
						searchquery += "AND "
					searchquery += "surname like %s " % ('"' + surname + '"')
					put = True
				if houseName != "":
					if put:
						searchquery += "AND "
					searchquery += "houseName like %s " % ('"' + houseName + '"')
	
	params['searchForm'] = searchStudentForm()

	query = ("SELECT userID, name, surname, houseName FROM student ") + searchquery
	cursor.execute(query)

	temp = []
	for userID, name, surname, houseName in cursor:
		if userID != request.user.id:
			t = {}
			t['userID'] = userID
			t['name'] = name
			t['surname'] = surname
			t['houseName'] = houseName
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


