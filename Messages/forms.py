from django import forms
from .models import Contact_Database

class DatabaseForm(forms.ModelForm):
    class Meta:
        model = Contact_Database
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'message']
