from django.urls import path
from. import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

app_name = 'vaciado'

urlpatterns = [
    path('', views.vaciado, name="vaciado"),#lista de vaciados    
    path('agregar/<int:w_pk>', views.add, name="add"),# nuevo vaciado
    
    path('borrar/<int:id>', views.delete, name="delete"), # borrar vaciado con Id
    path('editar-w/<int:id>', views.update, name="update"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)