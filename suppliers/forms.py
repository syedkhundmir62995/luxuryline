# from typing_extensions import Required
from email.policy import default
from django.db.models import query
from django.forms import ModelForm, fields
from django import forms
from suppliers.models import Scale,Material




class DateInput(forms.DateInput):
    input_type = "date"

class MaterialForm(forms.Form):
    mid = forms.CharField(max_length=200,required=True)
    material = forms.CharField(widget=forms.Textarea(),required=True)
    quantity = forms.IntegerField(max_value=10000,required=True)
    color = forms.CharField(max_length=200,required=True)
    lastupdated = forms.CharField(widget=DateInput)
    
class EditMaterialForm(forms.Form):
    mid = forms.CharField(max_length=200, required= True)
    quantity = forms.IntegerField(max_value=10000,required=True)
    lastupdated = forms.CharField(widget=DateInput)

class SupplierForm(forms.Form):
    suppliername = forms.CharField(max_length=200,required=True)
    supplieraddress = forms.CharField(max_length=200,required=True)
    vat = forms.CharField(max_length=200,required=False)

# class ViewMaterialForm(forms.Form):
#     mid = forms.CharField(max_length=200, required=True)
#     material_name = forms.CharField(max_length=200,required=True)
#     quantity = forms.IntegerField(max_value=10000,required=True)
#     date = forms.CharField(widget=DateInput)
