import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from HarryPotter.settings import cnx, cursor

class editStaffForm(forms.Form):
	name = forms.CharField()
	surname = forms.CharField()

class editStudentForm(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    houseChoices = (
            ('Gryffindor', 'Gryffindor'),
            ('Hufflepuff', 'Hufflepuff'),
            ('Ravenclaw', 'Ravenclaw'),
            ('Slytherin', 'Slytherin'),
        )
    houseName = forms.ChoiceField(choices=houseChoices)