from django import forms
from .models import Life_Style_Database

class DatabaseForm(forms.ModelForm):
    class Meta:
        model = Life_Style_Database
        fields = ['name', 'email']
