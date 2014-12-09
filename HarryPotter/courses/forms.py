import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from HarryPotter.settings import cnx, cursor

class courseForm(forms.Form):
    name = forms.CharField(required=True)
    room = forms.IntegerField()
    description = forms.CharField()
    timetable = forms.CharField()

class searchCourseForm(forms.Form):
	id = forms.IntegerField()
	name = forms.CharField()
	room = forms.IntegerField()