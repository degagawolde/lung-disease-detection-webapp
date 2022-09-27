from django.urls import path
from . import views
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('predict', views.predictImage, name='predict'),
    path('viewdb', views.viewDataBase, name='view'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)