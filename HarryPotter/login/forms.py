import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
 
class LoginForm(forms.Form):
 
    username = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)))
    password = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)))
