from django import forms
from .models import Mental_Health_Database

class DatabaseForm(forms.ModelForm):
    class Meta:
        model = Mental_Health_Database
        fields = ['name', 'email']
