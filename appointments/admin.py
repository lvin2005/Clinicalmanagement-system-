from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'appointment_date', 'appointment_type', 'status', 'created_at')
    list_filter = ('status', 'appointment_type', 'appointment_date', 'created_at')
    search_fields = ('patient__first_name', 'patient__last_name', 'doctor__user__first_name', 'doctor__user__last_name', 'reason')
    ordering = ('-appointment_date',)
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('patient', 'doctor', 'appointment_date', 'appointment_type', 'status')
        }),
        ('Medical Information', {
            'fields': ('reason', 'notes', 'symptoms', 'blood_pressure', 'heart_rate', 'temperature', 'weight', 'height')
        }),
        ('Treatment', {
            'fields': ('prescription', 'follow_up_date')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('created_at',)
        return self.readonly_fields
