from welcome.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponseRedirect
from django.template import RequestContext
 
@csrf_protect
def register(request, template_name, redirect_name):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return redirect(redirect_name)
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render(request, template_name, variables)
 
def register_success(request, template_name):
    return render(request, template_name)
 
def logout_page(request, redirect_name):
    logout(request)
    return redirect(redirect_name)
 