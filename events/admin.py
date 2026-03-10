from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'event_date', 'capacity', 'created_at')
    list_filter = ('event_date', 'location')
    search_fields = ('title', 'description', 'location')
    date_hierarchy = 'event_date'
    ordering = ('-event_date',)
