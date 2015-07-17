from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError

def index(request):
    if request.POST:
        form = AuthenticationForm(data=request.POST)
        try:
            if form.is_valid():
                login(request,form.get_user())
            else:
                HttpResponse('authentication failed')
        except ValidationError:
             HttpResponse("Authentication failed - wrong password/login or user is not active or can't set cookies")
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'questions.html', context)
