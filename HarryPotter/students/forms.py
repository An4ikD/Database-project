import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from HarryPotter.settings import cnx, cursor

class searchStudentForm(forms.Form):
	id = forms.IntegerField()
	name = forms.CharField()
	surname = forms.CharField()
	houseName = forms.CharField()