from django.contrib import admin
from .models import Mental_Health_Database

@admin.register(Mental_Health_Database)
class Database_Admin(admin.ModelAdmin):
    list_display = ('name', 'email', 'id')
    search_fields = ('name', 'email')
    list_filter = ('name', 'email')