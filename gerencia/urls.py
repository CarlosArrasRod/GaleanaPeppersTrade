from django.urls import path
from. import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

app_name = 'gerencia'

urlpatterns = [
    path('', views.gerente, name="gerente"),
    path('graficas/data/<int:mes>/<int:anio>/', views.graficas, name="graficas"),
    path('pesa/', views.gerencia_weight, name="weight"),
    path('vaciado/', views.gerencia_vaciado, name="vaciado"),
    path('production/', views.gerencia_production, name="production_list"),
    path('pipas/', views.gerencia_pipa, name="pipas_list"),
    path('calidad/', views.gerencia_calidad, name="calidad_lista"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)