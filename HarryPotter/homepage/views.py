from django.shortcuts import render

def view(request, template_name):
	params = {}
	return render(request, template_name, params)