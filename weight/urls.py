from django.urls import path
from. import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

app_name = 'weight'

urlpatterns = [
    # path('/',views.dashboard.as_view(), name="dashboard"),
    path('', views.weight, name="weight"),
    path('agregar-w', views.add, name="add"),
    path('editar-w', views.update, name="update"),
    path('borrar/<int:id>', views.delete, name="delete"),
    path('editar/<int:id>', views.update, name="update"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)