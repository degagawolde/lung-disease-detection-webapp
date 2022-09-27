from django.urls import path
from .views import *
from .views import PicList, PicDetail, PicAdd, PicDelete

app_name = "DiseaseClassification"

print(PicList)
urlpatterns = [
    path('',PicList.as_view(),name='list'),
    path('<int:pk>/',PicDetail.as_view(),name='detail'),
    path('add/',PicAdd.as_view(),name='add'),
    path('<int:pk>/delete/',PicDelete.as_view(),name='delete'),
]
