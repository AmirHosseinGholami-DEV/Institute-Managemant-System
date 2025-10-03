from django.contrib import admin
from .models import Contact_Database

@admin.register(Contact_Database)
class DatabaseFormAdmin(admin.ModelAdmin):
    list_display = ('id','first_name', 'last_name', 'email', 'phone_number', 'message')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number', 'message')
    list_filter = ('first_name', 'last_name', 'email', 'message')
