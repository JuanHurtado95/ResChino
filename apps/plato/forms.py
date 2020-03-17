from django import forms
from .models import ingredientes

class ingredientesForm(forms.ModelForm):
    class Meta:
        model = ingredientes
        fields = ['nombre', 'tipo', 'precio'] 
