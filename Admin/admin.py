from django.contrib import admin
from .models import Student_Database

@admin.register(Student_Database)
class DatabaseFormAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'grade', 'number', 'Amount')
    search_fields = ('name', 'grade')
    list_filter = ('name', 'grade', 'number', 'Amount')