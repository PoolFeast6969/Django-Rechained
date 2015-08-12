from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.signals import user_logged_in
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

def index(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'questions.html', context)

def login(request, template_name='login.html'):
    messages.add_message(request, messages.INFO, "logged in")
    return auth_views.login(request, template_name)

def logout(request, next_page='/'):
    messages.add_message(request, messages.INFO, "logged out")
    return auth_views.logout(request, next_page)
