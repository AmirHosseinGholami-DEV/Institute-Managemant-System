from django.utils.html import format_html
from django.contrib import admin
from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio', 'display_photo')
    search_fields = ('name', 'bio')
    list_filter = ('name',)

    def display_photo(self, obj):
        return format_html('<img src="{}" width="50" height="50" border-radius="12" />', obj.photo.url)

    display_photo.short_description = 'Photo'