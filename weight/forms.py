from django import forms
from .models import Weight

class WeightForm(forms.ModelForm):
    class Meta:
        model = Weight
        fields = '__all__'