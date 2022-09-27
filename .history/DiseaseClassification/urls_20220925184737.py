from django.urls import path
from DiseaseClassification import views

urlpatterns = [
    path('', views.home, name="home"),
    path('predict', views.predictImage, name='predict'),
    path('viewdb', views.viewDataBase, name='view'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)