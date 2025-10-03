from django import forms
from .models import Rhetorical_Database

class DatabaseForm(forms.ModelForm):
    class Meta:
        model = Rhetorical_Database
        fields = ['name', 'email']
