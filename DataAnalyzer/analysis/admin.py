from django.contrib import admin
from .models import UploadedFile
from django.utils.html import format_html
# Register your models here.

@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
    """
    Admin configuration for the UploadedFile model.
    """
    # Fields to display in the list view of the admin panel
    list_display = ('file', 'display_first_rows', 'display_missing_values')
    readonly_fields = ('display_first_rows', 'display_missing_values') #read-only filds

    def display_first_rows(self, obj):
        return format_html(obj.first_rows)
    display_first_rows.short_description = 'First Rows'

    def display_missing_values(self, obj):
        return format_html(obj.missing_values)
    display_missing_values.short_description = 'Missing Values'
    
    # Define the layout of the fields in the admin form
    fieldsets = (
        (None, {
            'fields': ('file',) #first section
        }),
        ('Analysis Results', {
            'fields': ('display_first_rows', 'display_missing_values'), #secons Section
        }),
    )
