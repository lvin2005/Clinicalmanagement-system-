from django.contrib import admin
from .models import MedicalRecord, MedicalFile

@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'title', 'record_type', 'record_date', 'is_confidential', 'created_at')
    list_filter = ('record_type', 'is_confidential', 'record_date', 'created_at')
    search_fields = ('patient__first_name', 'patient__last_name', 'doctor__user__first_name', 'doctor__user__last_name', 'title', 'diagnosis')
    ordering = ('-record_date',)
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('patient', 'doctor', 'record_type', 'title', 'record_date', 'is_confidential')
        }),
        ('Medical Information', {
            'fields': ('description', 'diagnosis', 'treatment', 'prescription', 'notes')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(MedicalFile)
class MedicalFileAdmin(admin.ModelAdmin):
    list_display = ('filename', 'medical_record', 'file_type', 'file_size', 'uploaded_at', 'uploaded_by')
    list_filter = ('file_type', 'uploaded_at')
    search_fields = ('filename', 'medical_record__title')
    ordering = ('-uploaded_at',)
    readonly_fields = ('uploaded_at', 'file_size')
