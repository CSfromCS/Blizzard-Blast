from django import forms
from .models import *

class OrderSlipForm(forms.ModelForm):
    class Meta:
        model = OrderSlip
        exclude = ()

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        exclude = ()

class ItemAddOnForm(forms.ModelForm):
    class Meta:
        model = ItemAddOn
        exclude = ()