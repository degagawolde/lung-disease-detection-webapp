from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
# Create your views here.

import re

def home(request):
    return HttpResponse("Hello, Django!")

def hello_there(request, name):
    return render(
        request,
        './hello.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )