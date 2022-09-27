from django import forms
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import UploadFileForm

from datetime import datetime
import urllib, base64
import re,os,io
# import cv2

def home(request):
    return render(request,'index.html')

def hello_there(request, name):
    data = {
            'name': name,
            'date': datetime.now()
            }
    return render( request, 'hello.html', data)
    
def upload_file(request):
    files=[]
    if request.method == 'POST' and request.FILES['myfile']:
        form = UploadFileForm(request.POST, request.FILES)
        myfiles = request.FILES.getlist('myfile')
        fs = FileSystemStorage()
        for f in myfiles:
            filename = fs.save(f.name,f)
            filepath = fs.path(filename)
            uploaded_file_url = fs.url(filename)
            files.append(filename)
        name = os.path.splitext(files[0])[0]
      
        # image = cv2.rdrecord('media/'+name)