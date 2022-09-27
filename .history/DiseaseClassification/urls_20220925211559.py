from django.urls import path
from DiseaseClassification import views

urlpatterns = [
    path('upload', views.home, name='upload'),
    path("classify/<name>",views.home,name='classification')
]