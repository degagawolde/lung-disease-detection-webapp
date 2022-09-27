from django import forms
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import UploadFileForm


import re,os

def home(request):
    return render(request,'index.html')

def hello_there(request, name):
    return render(
        request,
        'hello.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )
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
      record = wfdb.rdrecord('media/'+name, sampto=500)
      # wfdb.plot_wfdb(record=record, 
      #             plot_sym=True,time_units='seconds',
      #             title='Record 100', figsize=(10,6),

      #             ecg_grids='all')
      wfdb.plot_items(signal=record.p_signal,
                      title='ECG Signal Plot', time_units='seconds',
                      fs=100,
                      ylabel =['I','II','III','AVR','AVL','AVF','V1','V2','V3','V4','V5','V6'],
                      sig_units=['mV', 'mV', 'mV', 'mV',
                                 'mV', 'mV', 'mV', 'mV',
                                 'mV', 'mV', 'mV', 'mV'],
                      figsize=(10, 8), ecg_grids='all')