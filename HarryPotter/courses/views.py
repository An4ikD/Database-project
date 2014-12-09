from django.shortcuts import render, redirect
from my_profile.views import *
from HarryPotter.settings import cnx, cursor
from django.http import HttpResponse
from courses.forms import *

trash = "(),"
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

	searchquery = ""

	if request.method == 'POST':
		searchForm = searchCourseForm(request.POST)
		if searchForm.is_valid:
			id = request.POST.get('id')
			name = request.POST.get('name')
			room = request.POST.get('room')
			
			if id == "" and name == "" and room == "":
				pass
			else:
				searchquery += "WHERE "
				put = False

				if id != "":
					searchquery += "ID like %s " % (id)
					put = True
				if name != "":
					if put:
						searchquery += "AND "
					searchquery += "name like %s " % ('"' + name + '"')
					put = True
				if room != "":
					if put:
						searchquery += "AND "
					searchquery += "room like %s " % (room)
	
	params['searchForm'] = searchCourseForm()


	query = ("SELECT ID, name, room, timetable, desciption FROM subject ") + searchquery
	print query
	cursor.execute(query)

	temp = []
	for ID, name, room, timetable, desciption in cursor:
		t = {}
		t['ID'] = ID
		t['name'] = name
		t['room'] = room
		t['timetable'] = timetable
		t['description'] = desciption
		temp.append(t)

	for i in temp:
		ID = i['ID']
		if userType == 2:
			query = ("SELECT subjectID, studentID FROM study "
					"WHERE subjectID like %s "
					"and studentID like %s" % (ID, userID))

			tmpCursor = cnx.cursor()
			tmpCursor.execute(query)

			for subjectID, studentID in tmpCursor:
				if subjectID == None:
					i['status'] = False
				else:
					i['status'] = True
					
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

def add_course(request, template_name, redirect_name):
	params = {}

	if request.method == 'POST':
		form = courseForm(request.POST)

		if form.is_valid():
			name = '"' + request.POST.get('name') + '"'
			room = request.POST.get('room')
			description = request.POST.get('description')
			timetable = request.POST.get('timetable')

			query = ("SELECT max(ID) from subject")
			cursor.execute(query)

			id = 0
			for ID in cursor:
				for i in ID:
					id = i + 1
			
			cnx.commit()
			query = ("INSERT INTO subject "
					"(ID, name) "
					"VALUES (%s, %s)" % (id, name))
			cursor.execute(query)
			cnx.commit()

			if room != "":
				query = ("UPDATE subject "
						"set room=%s " 
						"WHERE name like %s" % (room, name))
				cursor.execute(query)
				cnx.commit()
			if description != '':
				query = ("UPDATE subject "
						"set desciption=%s " 
						"WHERE name like %s" % ('"' + description + '"', name))
				cursor.execute(query)
				cnx.commit()
			if timetable != '':
				query = ("UPDATE subject "
						"set timetable=%s " 
						"WHERE name like %s" % ('"' + timetable + '"', name))
				cursor.execute(query)
				cnx.commit()

			return redirect(redirect_name)

	form = courseForm()
	params['form'] = form
	return render(request, template_name, params)

def teach_course(request, id, template_name):
	params = {}
	
	userID = request.user.id

	query = ("UPDATE subject "
            "set teacherID=%s "
            "WHERE ID=%s" % (userID, id))
	cursor.execute(query)
	cnx.commit()

	params['message'] = "You have successfully registered for teaching this course!"

	return render(request, template_name, params)


def edit_course(request, id, template_name, redirect_name):
	params = {}

	if request.method == 'POST':
		form = courseForm(request.POST)

		if form.is_valid():
			name = '"' + request.POST.get('name') + '"'
			room = request.POST.get('room')
			description = request.POST.get('description')
			timetable = request.POST.get('timetable')

			query = ("UPDATE subject "
					"set name=%s " 
					"WHERE ID like %s" % (name, id))
			cursor.execute(query)
			cnx.commit()

			if room != '':
				query = ("UPDATE subject "
						"set room=%s "
						"WHERE ID like %s" % (room, id))
				cursor.execute(query)
				cnx.commit()
			if description != '':
				query = ("UPDATE subject "
						"set desciption=%s "
						"WHERE ID like %s" % ('"' + description + '"', id))
				cursor.execute(query)
				cnx.commit()
			if timetable != '':
				query = ("UPDATE subject "
						"set timetable=%s "
						"WHERE ID like %s" % ('"' + timetable + '"', id))
				cursor.execute(query)
				cnx.commit()

			return redirect(redirect_name)

	form = courseForm()
	params['form'] = form
	params['id'] = id
	return render(request, template_name, params)

def delete_course(request, id, template_name):
	params = {}
	
	userID = request.user.id

	query = ("DELETE FROM study "
			"where subjectID like %s" % (id))
	cursor.execute(query)
	cnx.commit()

	query = ("DELETE FROM subject "
            "where ID like %s" % (id))
	cursor.execute(query)
	cnx.commit()

	params['message'] = "You have successfully deleted this course!"

	return render(request, template_name, params)
