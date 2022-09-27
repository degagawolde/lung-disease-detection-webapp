from django.shortcuts import render

from django.core.files.storage import FileSystemStorage
from .models import Result
from rest_framework.views import APIView
from rest_framework.response import Response
# from .serializers import LeafDiseaseSerializer  


import numpy as np
import joblib as jb
import json 
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 


img_height, img_width = 256, 256
with open('./models/labels.json', 'r') as f:
    labelInfo = f.read()

labelInfo = json.loads(labelInfo)
# print(labelInfo)

model=jb.load('./models/model.pkl')

# Create your views here.
def index(request):
    return render(request, 'index.html')

def predictImage(request):
    try:
        fileObj = request.FILES['filePath']
        fs = FileSystemStorage()

        filePathName = fs.save(fileObj.name, fileObj)
        filePathName = fs.url(filePathName)
        testimage = '.'+filePathName
        # print(testimage)
        # print(filePathName)

        # print(type(testimage))

        # if '%20' in testimage:
        #     testimage = fileObj.replace("%20", ' ')
        #     print(testimage)

        # img = image.load_img(testimage, target_size=(img_height, img_width))
        # test_image = image.img_to_array(img)
        test_image = np.expand_dims(test_image, axis = 0)

        confidence = 0
        pred = model.predict(test_image)
        confidence = round(np.max(pred) * 100, 2)

        predictedLabel = labelInfo[str(np.argmax(pred[0]))]
        print('Predicted label: ', predictedLabel)  
        print(f'Confidence : {confidence}%')    

        filename = filePathName.split('/')[-1]
        print(filename)

        new_item = Result(imagepath = filePathName , image = filename, predicted = predictedLabel, confidence = confidence)
        new_item.save()

        context = {'filePathName':filePathName, 'predictedLabel': predictedLabel, 'confidence': confidence, 'filename': filename}
        return render(request, 'index.html', context)

    except:
        return render(request, 'index.html')


def viewDataBase(request):
    all_results = Result.objects.all()

    for i in all_results:
        print(i.imagepath)
        break

    # listOfImages = os.listdir('./media/')
    # listOfImagesPath = ['./media/' + i for i in listOfImages]
    context = { 'all_results':all_results}  #  'listOfImagesPath': listOfImagesPath,
    return render(request, 'viewDB.html', context)
