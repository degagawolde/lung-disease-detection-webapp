from django.contrib import auth
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View
from django.views.generic import DeleteView
from django.urls import reverse_lazy
import json
import sys,os
sys.path.append("/Volumes/MLData/Python/yolov5/")
from mydetect import detect
import cv2
#import models
from .models import Diagnosis
# import form
from .forms import DiagnosisForm

class PicAdd(View):
    form = DiagnosisForm()
    template_name = 'MammoNetAii/breast_cancer_create.html'
    context = {"form":form}

    def get(self, request):
        return render(request,template_name=self.template_name,context=self.context)


    def post(self,request):
        createForm = DiagnosisForm(request.POST, request.FILES)
        print(createForm)
        if createForm.is_valid():
            print("It is valid")
            obj = createForm.save(commit=False)
            print("Prediction: ",obj.diagnosis)
            obj.save()
            image_path=obj.image.url
            image_path = os.path.join("media/images",image_path.split("/")[-1].replace("%20"," "))
            im= cv2.imread(image_path)
    
            r_image,_,obj_list=detect(weights='/Volumes/MLData/Python/yolov5/runs/train/exp26/weights/best.pt',path=image_path, data='/Volumes/MLData/Python/yolov5/data/breastnocalc.yaml')
       
            r_image = cv2.cvtColor(r_image, cv2.COLOR_BGR2RGB)
        
            cv2.imwrite(image_path,r_image)
            print(obj_list)
            obj.diagnosis=json.dumps(obj_list)
            #obj.diagnosis,obj.confidence = get_prediction(obj.image.url)
            obj.save()
            #obj.diagnosis,obj.confidence = detect_image_auto(obj.image.url)
            #obj.save()
            return redirect('MammoNetAii:list')

        return render(request,template_name=self.template_name,context=self.context)

# List all images in the dataset

class PicList(View):
    model = Diagnosis
    def get(self,request):
        template_name = 'MammoNetAii/breast_cancer_list.html'
        pictures = self.model.objects.all()
        context = {'pictures':pictures}

        return render(request,template_name=template_name,context=context)

# the detail of individual image

class PicDetail(View):
    model = Diagnosis
    #post method
    def get(self,request,pk):
        template_name = 'MammoNetAii/breast_cancer_detail.html'
        picture = self.model.objects.get(id = pk)
        dx = json.loads(picture.diagnosis)
        #dx=eval(dx.split()[0])
        
        context = {'picture':picture,'dx':dx}
        
        return render(request,template_name=template_name,context=context)

# delete individual image

class PicDelete(View):
    model = Diagnosis
    template_name = 'MammoNetAii/breast_cancer_delete.html'

    def get(self,request,pk):
        picture = self.model.objects.get(id = pk)

        context = {'picture':picture}

        return render(request,template_name=self.template_name,context=context)

    def post(self,request,pk):
       # delet object with Image Id
        query_set = self.model.objects.get(pk = pk)
        path=query_set.image.path
        #print(path)
        query_set.delete() 
        if os.path.exists(path):
            os.remove(path)
        return redirect('MammoNetAii:list')

