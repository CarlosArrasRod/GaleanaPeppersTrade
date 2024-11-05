from django.db import models
from weight.models  import Weight
# Create your models here.

class Vaciado(models.Model):
    id = models.AutoField(primary_key=True)
    weight = models.ForeignKey( Weight, related_name="vaciados",on_delete=models.CASCADE)
    hdecomiezov = models.TimeField()
    hdefinalizacionv = models.TimeField()
    hdecomiezobanda = models.TimeField()
    hdefinalizacionbanda = models.TimeField()
    tiempovaciado = models.TimeField()
    tiempodebanda = models.TimeField()

    def __str__(self):
        return self.weight.folio + " - " + "Fecha: " + str(self.weight.fecha) 
