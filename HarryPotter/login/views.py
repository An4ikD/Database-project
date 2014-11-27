from login.forms import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout


def sign_in(request, template_name, redirect_name):
	params = {}
	params['form'] = LoginForm()

	if request.method == 'POST':
		form = LoginForm(request.POST)
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)

		if user is not None:
			# the password verified for the user
			if user.is_active:
				login(request, user)
				return redirect(redirect_name)
			else:
				return render(request, template_name)
		else:
			# the authentication system was unable to verify the username and password
			params['error'] = "The username or password was incorrect."
			return render(request, template_name, params)

	return render(request, template_name, params)

def sign_out(request, redirect_name):
	logout(request)
	return redirect(redirect_name)