from dataclasses import field
from django.core import validators
from django import forms
from .models import Add_Service

class addservice(forms.ModelForm):
    class Meta:
        model=Add_Service
        fields=['service_name','service_charge','service_desc']
        widgets = {
            'service_name':forms.TextInput(attrs={'class':'form-control'}),
            'service_charge':forms.TextInput(attrs={'class':'form-control'}),
            'service_desc':forms.TextInput(attrs={'class':'form-control'}),
        }
