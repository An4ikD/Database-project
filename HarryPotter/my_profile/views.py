from my_profile.forms import profileEditForm
import mysql.connector
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext

cnx = mysql.connector.connect(
    user='a.dikhanov',
    password= 'I11ustrator',
    host= '10.10.200.67',
    database= 'anuar_dikhanov_project', 
    raise_on_warnings= True,
)
cursor = cnx.cursor()

@login_required
def my_profile(request, template_name):
	params = {}
	params['user'] = request.user
	return render(request, template_name, params)

def edit(request, template_name, redirect_name):
    if request.method == 'POST':
        form = profileEditForm(request.POST)
        
        if form.is_valid():
            add_employee = ("INSERT INTO staff "
               "(userID, name, surname, username, password) "
               "VALUES (%s, %s, %s, %s, %s)")

            data_employee = (
            	request.user.id,
            	request.POST.get('name'),
            	request.POST.get('surname'),
            	request.user.username,
            	request.user.password
            )
            cursor.execute(add_employee, data_employee)
            cnx.commit()
            
            return redirect(redirect_name)
    else:
        form = profileEditForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render(request, template_name, variables)

def search_students(request, template_name):
    return render(request, template_name)

def search_staff(request, template_name):
    return render(request, template_name)

def search_subjects(request, template_name):
    return render(request, template_name)

def logout_page(request, redirect_name):
    logout(request)
    return redirect(redirect_name)
