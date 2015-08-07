from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'questions.html', context)
