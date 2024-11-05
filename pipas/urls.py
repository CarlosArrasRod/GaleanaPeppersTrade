from django.urls import path
from. import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

app_name = 'pipas'

urlpatterns = [
    path('', views.pipas, name="pipas_list"),
    path('agregar/<int:w_pk>', views.add, name="add"),
    
    path('borrar/<int:id>', views.delete, name="delete"),
    path('editar/<int:id>', views.update, name="update"),
    
    path('CBV_crear/', views.Agregar_CreateView.as_view(), name='create_pipa')
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)