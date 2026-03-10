from django.db import models
from django.contrib.auth.models import User
from events.models import Event

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    number_of_tickets = models.IntegerField(default=1)
    booking_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.event.title}"
    
    class Meta:
        ordering = ['-booking_date']
