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
        
        mpimg.imread(uploaded_file_url,cmap='gray')
        fig = plt.gcf()
        #convert graph into dtring guffer and then we convert 64 bit code into image
        buf = io.BytesIO()
        fig.savefig(buf,format='png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri = urllib.parse.quote(string)
      
        return TemplateResponse(request, 'upload.html', {
            'uploaded_file_url': uploaded_file_url,
            'text': 'Upload Chest x-ray Image',
            'data':uri
        })
    
    return render(request, 'upload.html',data)