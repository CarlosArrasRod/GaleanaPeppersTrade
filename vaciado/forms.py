from django import forms
from .models import Vaciado


class VaciadoForm(forms.ModelForm):
    class Meta:
        model = Vaciado
        fields = '__all__'
        widgets ={
            #'weight':forms.HiddenInput(),
        }
