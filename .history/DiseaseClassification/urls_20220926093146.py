from django.urls import path
from DiseaseClassification import views

urlpatterns = [
    path('', views.home, name="home"),
    path('choose/',views.upload_file_form,name="choosefile"),
    path('upload/',views.upload_file_request,name='uploadfile'),
    path("classify/<name>",views.home,name='classification')
]