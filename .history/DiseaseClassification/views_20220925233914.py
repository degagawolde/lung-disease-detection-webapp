from django import forms
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.template import loader
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import UploadFileForm

from datetime import datetime
import urllib, base64
# import re,os,io
# import cv2

def home(request):
    return render(request,'index.html',context=data)

def upload_file(request):
    data = {'name':'EAII',
            'text':'Upload Chest x-ray Image'}
    files=[]
    if request.method == 'POST' and request.FILES['myfile']:
       if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        print(myfile)
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        
        return TemplateResponse(request, 'upload.html', {
            'uploaded_file_url': uploaded_file_url,
            'text': 'Upload Chest x-ray Image'
        })
    
    return render(request, 'upload.html',data)