from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView
from django.utils import timezone
from events.models import Event
from .models import Booking
from .forms import BookingForm

@login_required
def create_booking(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.event = event
            booking.save()
            messages.success(request, f'Booking confirmed for {event.title}!')
            return redirect('pages:dashboard')
    else:
        form = BookingForm(initial={'event': event})
    
    return render(request, 'bookings/create_booking.html', {
        'form': form,
        'event': event,
    })

class UserBookingListView(ListView):
    model = Booking
    template_name = 'bookings/user_bookings.html'
    context_object_name = 'bookings'
    
    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user).order_by('-booking_date')
