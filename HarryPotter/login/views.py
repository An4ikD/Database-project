from django.shortcuts import render

def login(request, template_name):
	return render(request, template_name)
