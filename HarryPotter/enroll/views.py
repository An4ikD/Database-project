from django.shortcuts import render
from enroll.forms import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from HarryPotter.settings import cnx, cursor

@csrf_protect
def enroll(request, template_name, redirect_name):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email'],
            )

            username = user.username
            password = user.password
            id = user.id
            userType = request.POST.get('userType')

            add_user = ("INSERT INTO user "
               "(ID, userType) "
               "VALUES (%s, %s)")

            data_user = (
                id,
                userType,
            )

            cursor.execute(add_user, data_user)
            cnx.commit()

            insert_to_type = ("")
            data_to_type = ()

            if userType == "1":
                insert_to_type = ("INSERT INTO staff "
                    "(userID, username, password)"
                    "VALUES (%s, %s, %s)")
                data_to_type = (
                    id, username, password
                )

            if userType == "2":
                insert_to_type = ("INSERT INTO student "
                    "(userID, username, password)"
                    "VALUES (%s, %s, %s)")
                data_to_type = (
                    id, username, password
                )
            print insert_to_type
            print data_to_type
            cursor.execute(insert_to_type, data_to_type)
            cnx.commit()

            return redirect(redirect_name)
    else:
        form = RegistrationForm()
    
    params = RequestContext(request, {
    'form': form
    })
    return render(request, template_name, params)

def enroll_success(request, template_name):
    return render(request, template_name)