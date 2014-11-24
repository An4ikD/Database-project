from django.shortcuts import render

def view(request, template_name):
	return render(request, template_name)