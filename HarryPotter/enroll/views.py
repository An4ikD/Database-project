from django.shortcuts import render
from enroll.forms import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext

@csrf_protect
def enroll(request, template_name, redirect_name):
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
    
    params = RequestContext(request, {
    'form': form
    })
    return render(request, template_name, params)

def enroll_success(request, template_name):
    return render(request, template_name)