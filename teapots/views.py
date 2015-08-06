from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError

def index(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'questions.html', context)
