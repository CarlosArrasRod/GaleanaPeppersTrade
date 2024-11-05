from django.db import models

# Create your models here.
class Weight(models.Model):
    class tp(models.TextChoices):
        n='cayenne','Cayenne'
        e='chipotle','Chipotle'
    id = models.AutoField(primary_key=True)
    folio = models.CharField(max_length=10, verbose_name='Folio')
    tproducto = models.CharField(max_length=50, choices=tp.choices, verbose_name=("tipoproducto"))
    fecha = models.DateField(verbose_name=("Fecha"))
    prodoembarc = models.CharField(max_length=50, verbose_name=("poe"))
    proveedor = models.CharField(max_length=50, verbose_name=("proveedor"))
    nombrechof = models.CharField(max_length=50, verbose_name=("nombrechof"))
    pesoton = models.FloatField()
    pesolib = models.FloatField(blank=True, null=True)
    horallegada = models.TimeField()
    horaapertura = models.TimeField()
    horacarga = models.TimeField()
    horasalida = models.TimeField()
    tiempoenfila = models.CharField(max_length=20)
    
    #def Aqui va la definicion para convertir automaticamente el toneladas a libras <3
    def save(self, *args, **kwargs):
        if self.pesoton:
            self.pesolib = self.pesoton * 2.20462
        super(Weight, self).save(*args, **kwargs)

    def __str__(self):
        fila = "Folio: " + self.folio + " - " + "TProducto: " + self.tproducto + " - Fecha: " + str(self.fecha)
        return fila
    
    class Meta:
        db_table='weight'