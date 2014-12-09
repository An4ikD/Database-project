from django.shortcuts import render, redirect
from my_profile.views import *
from HarryPotter.settings import cnx, cursor
from houses.forms import *

def get_houses(request, template_name):
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
		searchForm = searchHouseForm(request.POST)
		if searchForm.is_valid:
			name = request.POST.get('name')
			symbol = request.POST.get('symbol')
			place = request.POST.get('place')
			traits = request.POST.get('traits')

			if place == "" and name == "" and symbol == "" and traits == "":
				pass
			else:
				searchquery += "WHERE "
				put = False

				if place != "":
					searchquery += "place like %s " % ('"' + place + '"')
					put = True
				if name != "":
					if put:
						searchquery += "AND "
					searchquery += "name like %s " % ('"' + name + '"')
					put = True
				if symbol != "":
					if put:
						searchquery += "AND "
					searchquery += "symbol like %s " % ('"' + symbol + '"')
					put = True
				if traits != "":
					if put:
						searchquery += "AND "
					searchquery += "traits like %s " % ('"' + traits + '"')
					put = True
	
	params['searchForm'] = searchHouseForm()

	query = ("SELECT name, symbol, place, traits FROM house ") + searchquery

	cursor.execute(query)

	temp = []
	for name, symbol, place, traits in cursor:
		t = {}
		t['name'] = name
		t['symbol'] = symbol
		t['place'] = place
		t['traits'] = traits
		temp.append(t)

	params['houses'] = temp

	return render(request, template_name, params)

def add_house(request, template_name, redirect_name):
	params = {}

	if request.method == 'POST':
		form = courseForm(request.POST)
		if form.is_valid:
			name = '"' + request.POST.get('name') + '"'
			symbol = request.POST.get('symbol')
			place = request.POST.get('place')
			traits = request.POST.get('traits')

			query = ("INSERT INTO house "
					"(name) "
					"VALUES (%s)" % (name))
			cursor.execute(query)
			cnx.commit()

			if symbol != '':
				query = ("UPDATE house "
						"set symbol=%s " 
						"WHERE name like %s" % ('"' + symbol + '"', name))
				cursor.execute(query)
				cnx.commit()
			if place != '':
				query = ("UPDATE house "
						"set place=%s " 
						"WHERE name like %s" % ('"' + place + '"', name))
				cursor.execute(query)
				cnx.commit()
			if traits != '':
				query = ("UPDATE house "
						"set traits=%s " 
						"WHERE name like %s" % ('"' + traits + '"', name))
				cursor.execute(query)
				cnx.commit()
			return redirect(redirect_name)

		else:
			params['error'] = "Please, enter the name of a house"

	form = courseForm()
	params['form'] = form
	return render(request, template_name, params)

def edit_house(request, houseName, template_name, redirect_name):
	params = {}

	if request.method == 'POST':
		form = courseForm(request.POST)

		if form.is_valid():
			name = '"' + request.POST.get('name') + '"'
			symbol = request.POST.get('symbol')
			place = request.POST.get('place')
			traits = request.POST.get('traits')

			query = ("UPDATE student "
					"set houseName=NULL "
					"WHERE houseName=%s" % (name))
			cursor.execute(query)
			cnx.commit()

			query = ("UPDATE house "
					"set name=%s " 
					"WHERE name like %s" % (name, '"' + houseName + '"'))
			cursor.execute(query)
			cnx.commit()

			if symbol != '':
				query = ("UPDATE house "
						"set symbol=%s "
						"WHERE name like %s" % ('"' + symbol + '"', '"' + houseName + '"'))
				cursor.execute(query)
				cnx.commit()
			if place != '':
				query = ("UPDATE house "
						"set place=%s "
						"WHERE name like %s" % ('"' + place + '"', '"' + houseName + '"'))
				cursor.execute(query)
				cnx.commit()
			if traits != '':
				query = ("UPDATE house "
						"set traits=%s "
						"WHERE name like %s" % ('"' + traits + '"', '"' + houseName + '"'))
				cursor.execute(query)
				cnx.commit()

			return redirect(redirect_name)

	form = courseForm()
	params['form'] = form
	params['name'] = houseName
	return render(request, template_name, params)

def delete_house(request, houseName, template_name):
	params = {}
	
	userID = request.user.id

	query = ("UPDATE student "
			"set houseName=NULL "
			"where houseName like %s" % ('"' + houseName + '"'))
	cursor.execute(query)
	cnx.commit()

	query = ("DELETE FROM house "
            "where name like %s" % ('"' + houseName + '"'))
	cursor.execute(query)
	cnx.commit()

	params['message'] = "You have successfully deleted this course!"

	return render(request, template_name, params)
