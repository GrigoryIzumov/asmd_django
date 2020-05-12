from django import forms
from django.forms import ClearableFileInput
from .models import DataModel


class DataModelForm(forms.ModelForm):
    class Meta:
        model = DataModel
        fields = ['file']
        widgets = {
            'file': ClearableFileInput(attrs={'multiple': True}),
        }
