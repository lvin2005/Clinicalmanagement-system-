from django.urls import path
from .views import create_booking, UserBookingListView

app_name = 'bookings'

urlpatterns = [
    path('create/<int:event_id>/', create_booking, name='create'),
    path('my-bookings/', UserBookingListView.as_view(), name='user_bookings'),
]
