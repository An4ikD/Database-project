import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
 
class profileEditForm(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()