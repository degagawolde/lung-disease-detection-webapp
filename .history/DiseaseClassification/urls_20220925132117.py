from django.urls import path
from DiseaseClassification import views

urlpatterns = [
    path("", views.home, name="home"),
    path("classify",views.hello_there('deagaa'),name='classification')
]