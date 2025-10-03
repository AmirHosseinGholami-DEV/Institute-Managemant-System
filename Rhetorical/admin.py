from django.contrib import admin
from .models import Rhetorical_Database

@admin.register(Rhetorical_Database)
class Database_Admin(admin.ModelAdmin):
    list_display = ('name', 'email', 'id')
    search_fields = ('name', 'email')
    list_filter = ('name', 'email')
