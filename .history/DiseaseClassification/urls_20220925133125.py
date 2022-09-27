from django.urls import path
from DiseaseClassification import views

urlpatterns = [
    path("", views.home, name="home"),
    path("classify/<name>",views.hello_there,name='classification')
]