from django.forms import ModelForm, widgets, TextInput, NumberInput
from .models import Product, Order
from django import forms


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "cost", "price", "quantity"]
        widgets = {"name": TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}),
                   "cost": NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter cost'}),
                   "price": NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price'}),
                   "quantity": NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter quantity'})}


class OrderForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    quantity = forms.IntegerField(widget=forms.NumberInput)