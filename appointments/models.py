from django.db import models
from django.utils import timezone
from patients.models import Patient
from doctors.models import Doctor

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('no_show', 'No Show'),
        ('rescheduled', 'Rescheduled'),
    ]

    TYPE_CHOICES = [
        ('consultation', 'Consultation'),
        ('follow_up', 'Follow-up'),
        ('emergency', 'Emergency'),
        ('surgery', 'Surgery'),
        ('checkup', 'Check-up'),
        ('vaccination', 'Vaccination'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    appointment_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    reason = models.TextField()
    notes = models.TextField(blank=True)
    symptoms = models.TextField(blank=True)
    blood_pressure = models.CharField(max_length=20, blank=True)
    heart_rate = models.PositiveIntegerField(blank=True, null=True)
    temperature = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    prescription = models.TextField(blank=True)
    follow_up_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient.full_name} - Dr. {self.doctor.full_name} on {self.appointment_date.strftime('%Y-%m-%d %H:%M')}"

    @property
    def is_past(self):
        return self.appointment_date < timezone.now()

    @property
    def is_today(self):
        return self.appointment_date.date() == timezone.now().date()

    def save(self, *args, **kwargs):
        if self.follow_up_date and self.follow_up_date <= self.appointment_date:
            self.follow_up_date = None
        super().save(*args, **kwargs)
