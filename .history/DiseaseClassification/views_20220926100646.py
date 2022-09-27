from django import forms
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.template import loader
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import UploadFileForm

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from datetime import datetime
import urllib, base64
import re,os,io
# import cv2

def home(request):
    data = {'text':'Upload Chest x-ray Image'}
    return render(request,'index.html',context=data)

def upload_file_form(request):
    data = {'name':'EAII',
            'text':'Upload Chest x-ray Image'}
    return render(request,'upload.html',data)

def upload_file_request(request):
    data = {'name':'EAII',
            'text':'Upload Chest x-ray Image'}
    files=[]
    if request.method == 'GET' and request.FILES:
       if request.method == 'GET' and request.FILES:
        myfile = request.FILES
        print(myfile)
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        
      
        return HttpResponse({
            'uploaded_file_url': uploaded_file_url,
            'text': 'Upload Chest x-ray Image'
        })
    
    return HttpResponse(data)