from django.db import models
from weight.models  import Weight
from vaciado.models  import Vaciado
# Create your models here.

class Production(models.Model):
    id = models.AutoField(primary_key=True)
    weight = models.ForeignKey(Weight, related_name="productions",on_delete=models.CASCADE)
    pdesal = models.FloatField()
    totalpasta = models.FloatField(blank=True, null=True)
    lotsal = models.CharField(max_length=30)
    lotsal2 = models.CharField(max_length=30)
    lotsal3 = models.CharField(max_length=30)
    kgdesal = models.FloatField(blank=True, null=True)
    tanque1 = models.CharField(max_length=30)
    tanque2 = models.CharField(max_length=30)
    tanque3 = models.CharField(max_length=30)
    lttanque1 = models.FloatField()
    lttanque2 = models.FloatField()
    lttanque3 = models.FloatField()
    ltpasta = models.FloatField(blank=True, null=True)
    kgpasta = models.FloatField(blank=True, null=True)
    kgdesperdiciados = models.FloatField(blank=True, null=True)
    
    
    def save(self, *args, **kwargs):
        pesoton = self.weight.pesoton or 0.0  # Si es None, se asigna 0.0
        kgdesal = self.kgdesal or 0.0         # Si es None, se asigna 0.0

        self.totalpasta = pesoton + kgdesal 
        

        
        if self.lttanque1:
            self.ltpasta = (self.lttanque1 or 0) + (self.lttanque2 or 0) + (self.lttanque3 or 0)
        if self.ltpasta:
            self.kgpasta = self.ltpasta * 1.14
        if self.kgpasta:
            self.kgdesperdiciados = self.kgpasta - pesoton
            super(Production, self).save(*args, **kwargs)
    def __str__(self):
        return f"Vaciado(PAPA ): {self.id} weight(Abuelo):{self.weight.folio}"