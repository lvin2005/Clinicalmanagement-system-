from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'specialization', 'license_number', 'phone', 'email', 'experience_years', 'created_at')
    list_filter = ('specialization', 'experience_years', 'created_at')
    search_fields = ('user__first_name', 'user__last_name', 'license_number', 'phone')
    ordering = ('user__last_name', 'user__first_name')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('User Information', {
            'fields': ('user',)
        }),
        ('Professional Information', {
            'fields': ('specialization', 'license_number', 'experience_years', 'consultation_fee')
        }),
        ('Contact Information', {
            'fields': ('phone', 'office_address')
        }),
        ('Availability', {
            'fields': ('available_days', 'available_time_start', 'available_time_end')
        }),
        ('Additional Information', {
            'fields': ('bio', 'education')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def email(self, obj):
        return obj.user.email
    email.short_description = 'Email'
