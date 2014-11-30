import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class editStaffForm(forms.Form):
	name = forms.CharField()
	surname = forms.CharField()

class editStudentForm(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    userTypeChoices = (
            ('1', 'Staff'),
            ('2', 'Student'),
            (),
            (),
        )
    houseName = forms.ChoiceField(choices=userTypeChoices)