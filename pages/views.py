from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from events.models import Event
from bookings.models import Booking
from blog.models import BlogPost

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def services(request):
    return render(request, 'pages/services.html')

@login_required
def dashboard(request):
    upcoming_events = Event.objects.filter(event_date__gte=timezone.now()).order_by('event_date')[:5]
    user_bookings = Booking.objects.filter(user=request.user).order_by('-booking_date')[:5]
    recent_posts = BlogPost.objects.all().order_by('-created_at')[:3]
    
    context = {
        'upcoming_events': upcoming_events,
        'user_bookings': user_bookings,
        'recent_posts': recent_posts,
    }
    return render(request, 'pages/dashboard.html', context)
