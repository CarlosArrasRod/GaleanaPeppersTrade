from django import forms
from .models import Pipas

class PipasForm(forms.ModelForm):
    class Meta:
        model = Pipas
        fields = '__all__'
        widgets = {
            'weight':forms.HiddenInput(),
        }