from django.urls import path
from. import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

app_name = 'production'

urlpatterns = [
    path('', views.production, name="production_list"),
    
    path('borrar/<int:id>', views.delete, name="delete"),
    path('CBV_crear/', views.Agregar_CreateView.as_view(), name='create_production'),
    
    path('editar/<int:pk>', views.Update_UpdateView.as_view(), name="update"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)