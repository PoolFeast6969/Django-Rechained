from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    import pdb; pdb.set_trace()
    return render(request, 'notice.html')
