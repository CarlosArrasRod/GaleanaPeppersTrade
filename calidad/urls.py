from django.urls import path
from. import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

app_name = 'calidad'

urlpatterns = [
    path('', views.calidad, name="calidad_lista"),#lista de vaciados    
    path('agregar/<int:w_pk>', views.add, name="add"),# nuevo vaciado
    
    path('', views.ListaCalidad_ListView.as_view(), name="CBV_lista"),
    path('CBV_crear/', views.Agregar_CreateView.as_view(), name="CBV_crear"),
    path('CBV_listaCalidades/', views.ListaCalidadesPeso_ListView.as_view(), name="CBV_listaCalidades"),
    path('CBV_Calidad_detailView/<int:pk>/', views.Calidad_detailView.as_view(), name="CBV_Calidad_detailView"),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)