from django.db import models
from weight.models  import Weight
# Create your models here.

class Calidad(models.Model):
    id = models.AutoField(primary_key=True)
    weight = models.ForeignKey( Weight, related_name="calidades",on_delete=models.CASCADE)
    causa = models.CharField(max_length= 50)
    tanque = models.CharField(max_length=30)
    tanque2 = models.CharField(max_length=30)
    hdecomiezo = models.TimeField()
    hdef = models.TimeField()
    ttotal= models.CharField(max_length=30, default=' ')

    def __str__(self):
        return self.weight.folio + " - " + "Fecha: " + str(self.weight.fecha) 
