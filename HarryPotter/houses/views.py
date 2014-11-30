from django.shortcuts import render
from my_profile.views import *
from HarryPotter.settings import cnx, cursor

def get_houses(request, template_name):
	params = {}

	userID = request.user.id
	userType = get_userType(userID)
	params['profile'] = get_profile(userType, userID)

	query = ("SELECT name, symbol, place FROM house ")

	cursor.execute(query)

	temp = []
	for name, symbol, place in cursor:
		t = {}
		t['name'] = name
		t['symbol'] = symbol
		t['place'] = place
		temp.append(t)

	params['houses'] = temp

	return render(request, template_name, params)