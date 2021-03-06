from my_profile.forms import editStaffForm, editStudentForm
import mysql.connector
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from HarryPotter.settings import cnx, cursor

trash = "()',"

def get_userType(userID):
    query = ("SELECT userType FROM user "
         "WHERE user.ID like %s" % userID)
    
    cursor.execute(query)

    userType = 3

    for i in cursor:
        for j in i:
            if j == 1:
                userType = 1
            else:
                userType = 2
    return userType

def get_profile(type, userID):
    if type == 1:
        query = ("SELECT name, surname FROM staff "
            "WHERE staff.userID like %s" % userID)
        
        cursor.execute(query)

        for name, surname in cursor:
            form = {
                'name': name,
                'surname': surname
            }
    else:
        query = ("SELECT name, surname, houseName FROM student "
            "WHERE student.userID like %s" % userID)
        
        cursor.execute(query)

        for name, surname, houseName in cursor:
            form = {
                'name': name,
                'surname': surname,
                'house': houseName
            }
    return form

@login_required
def my_profile(request, template_name):
    params = {}
    params['user'] = request.user

    userType = get_userType(request.user.id)

    if userType == 1:
        params['is_staff'] = True
        params['profile'] = get_profile(userType, request.user.id)

        query = ("SELECT subject.name FROM subject "
            "WHERE subject.teacherID like %s " % (request.user.id))
        cursor.execute(query)

        temp = []
        for course in cursor:
            courseName = ""
            for i in course:
                if i not in trash:
                    courseName += i

            temp.append({'course':courseName})

        params['courses'] = temp

    else:
        params['is_staff'] = False
        params['profile'] = get_profile(userType, request.user.id)

        query = ("SELECT subject.name FROM subject, study "
            "WHERE study.studentID like %s "
            "and study.subjectID like subject.ID" % (request.user.id))
        cursor.execute(query)

        temp = []
        for course in cursor:
            courseName = ""
            for i in course:
                if i not in trash:
                    courseName += i

            temp.append({'course':courseName})

        params['courses'] = temp

    return render(request, template_name, params)


def edit(request, template_name, redirect_name):
    userID = request.user.id
    userType = get_userType(userID)

    params = {}
    if userType == 1:
        params['is_staff'] = True
    else:
        params['is_staff'] = False
    if request.method == 'POST':
        if userType == 1:
            form = editStaffForm(request.POST)
            name = '"' + str(request.POST.get('name')) + '"'
            surname = '"' + str(request.POST.get('surname')) + '"'

            if form.is_valid():
                update_staff = ("UPDATE staff "
                   "SET name=%s, surname=%s "
                   "where staff.userID like %s" % (name, surname, userID))
                
                cursor.execute(update_staff)
                cnx.commit()
                return redirect(redirect_name)
        else:
            form = editStudentForm(request.POST)
            name = '"' + str(request.POST.get('name')) + '"'
            surname = '"' + str(request.POST.get('surname')) + '"'
            houseName = '"' + str(request.POST.get('houseName')) + '"'

            if form.is_valid():
                update_student = ("UPDATE student "
                   "SET name=%s, surname=%s, houseName=%s"
                   "where student.userID like %s" % (name, surname, houseName, userID))
                
                cursor.execute(update_student)
                cnx.commit()
                return redirect(redirect_name)

    if userType == 1:
        params['form'] = editStaffForm()
        params['profile'] = get_profile(userType, request.user.id)
    else:
        params['form'] = editStudentForm()
        params['profile'] = get_profile(userType, request.user.id)

    return render(request, template_name, params)

def logout_page(request, redirect_name):
    logout(request)
    return redirect(redirect_name)
