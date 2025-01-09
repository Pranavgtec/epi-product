from django import forms
from .models import ProductScheme

class ProductSchemeForm(forms.ModelForm):
    class Meta:
        model = ProductScheme
        fields = ['product_id', 'investment', 'total', 'days']