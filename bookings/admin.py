from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'number_of_tickets', 'booking_date')
    list_filter = ('booking_date', 'event')
    search_fields = ('user__username', 'event__title')
    date_hierarchy = 'booking_date'
    ordering = ('-booking_date',)
