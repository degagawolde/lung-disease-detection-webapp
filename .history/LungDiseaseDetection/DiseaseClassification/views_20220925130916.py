from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
# Create your views here.

def home(request):
    return HTTPResponse("Hello, Django!")

def hello_there(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )