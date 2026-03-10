from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Event

class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'
    
    def get_queryset(self):
        return Event.objects.filter(event_date__gte=timezone.now()).order_by('event_date')

class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'
