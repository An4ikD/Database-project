import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from HarryPotter.settings import cnx, cursor

class courseForm(forms.Form):
    name = forms.CharField(required=True)
    symbol = forms.CharField()
    place = forms.CharField()
    traits = forms.CharField()

class searchHouseForm(forms.Form):
	name = forms.CharField()
	symbol = forms.CharField()
	place = forms.CharField()
	traits = forms.CharField()