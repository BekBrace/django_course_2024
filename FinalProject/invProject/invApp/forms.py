from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'product_id': 'Product ID',
            'name': 'Name',
            'sku': 'SKU',
            'price': 'Price',
            'quantity': 'Quantity',
            'supplier': 'Supplier',
        }
        widgets = {
            'product_id': forms.NumberInput(
                attrs={'placeholder':'e.g. 1', 'class':'form-control'}),
            'name': forms.TextInput(
                attrs={'placeholder':'e.g. shirt', 'class':'form-control'}),
            'sku': forms.TextInput(
                attrs={'placeholder':'e.g. S12345', 'class':'form-control'}),
            'price': forms.NumberInput(
                attrs={'placeholder':'e.g. 19.99', 'class':'form-control'}),
            'quantity': forms.NumberInput(
                attrs={'placeholder':'e.g. 10', 'class':'form-control'}),
            'supplier': forms.TextInput(
                attrs={'placeholder':'e.g. ABC Corp', 'class':'form-control'}),
        }