from django import forms
from .models import Production

class ProductionForm(forms.ModelForm):
    class Meta:
        model = Production
        fields = '__all__'
        widgets = {
            'weight':forms.HiddenInput(),
        }