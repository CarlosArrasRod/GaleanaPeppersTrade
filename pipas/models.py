from django.db import models
from weight.models  import Weight
# Create your models here.
class Pipas(models.Model):
    id = models.AutoField(primary_key=True)
    weight = models.ForeignKey( Weight, related_name="pipa",on_delete=models.CASCADE)
    bol = models.CharField(max_length=50)
    selloasup = models.CharField(max_length=50)
    sellodesc = models.CharField(max_length=50)
    selloasup2 = models.CharField(max_length=50)
    sellodesc2 = models.CharField(max_length=50)
    sellorep = models.CharField(max_length=50)
    bombac = models.CharField(max_length=50, default=' ')
    tanque1 = models.CharField(max_length=50)
    tanque2 = models.CharField(max_length=50)
    horacarga = models.TimeField()
    horafcarga = models.TimeField()
    tiempocarga = models.CharField(max_length=20)

    def __str__(self):
        fila = "Folio: " + self.weight.folio + " - " + " - Fecha: " + str(self.weight.fecha) + " - Id: " + self.weight.proveedor 
        return fila
    
    class Meta:
        db_table='pipas'