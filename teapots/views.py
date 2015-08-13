from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User as user
from django.contrib.auth.signals import user_logged_in
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

def index(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'questions.html', context)

def login(request, template_name='login.html'):
    response = auth_views.login(request, template_name)
    if request.user.is_authenticated():
        messages.info(request, 'logged in')
    else:
        messages.error(request, 'there was a problem with your login')
    return response

def logout(request, next_page='/'):
    response = auth_views.logout(request, next_page)
    if request.user.is_authenticated():
        messages.error(request, 'there was a problem with your logout.....somehow')
    else:
        messages.info(request, 'logged out')
    return response
