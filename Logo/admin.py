from django.contrib import admin
from .models import Logo_Database

@admin.register(Logo_Database)
class Database_Admin(admin.ModelAdmin):
    list_display = ('name', 'email', 'id')
    search_fields = ('name', 'email')
    list_filter = ('name', 'email')
