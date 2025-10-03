from django import forms
from .models import Logo_Database

class DatabaseForm(forms.ModelForm):
    class Meta:
        model = Logo_Database
        fields = ['name', 'email']
