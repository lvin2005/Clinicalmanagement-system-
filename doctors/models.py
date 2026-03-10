from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    SPECIALIZATION_CHOICES = [
        ('GP', 'General Practitioner'),
        ('CARD', 'Cardiologist'),
        ('DERM', 'Dermatologist'),
        ('ENDO', 'Endocrinologist'),
        ('GAST', 'Gastroenterologist'),
        ('NEPH', 'Nephrologist'),
        ('NEUR', 'Neurologist'),
        ('ONCO', 'Oncologist'),
        ('OPHT', 'Ophthalmologist'),
        ('ORTH', 'Orthopedic Surgeon'),
        ('PATH', 'Pathologist'),
        ('PED', 'Pediatrician'),
        ('PSYC', 'Psychiatrist'),
        ('RAD', 'Radiologist'),
        ('SURG', 'Surgeon'),
        ('UROL', 'Urologist'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=4, choices=SPECIALIZATION_CHOICES)
    license_number = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=20)
    office_address = models.TextField()
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)
    available_days = models.CharField(max_length=100, help_text="e.g., Monday, Tuesday, Wednesday")
    available_time_start = models.TimeField()
    available_time_end = models.TimeField()
    bio = models.TextField(blank=True)
    education = models.TextField(blank=True)
    experience_years = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Dr. {self.user.get_full_name() or self.user.username} - {self.get_specialization_display()}"

    @property
    def full_name(self):
        return self.user.get_full_name() or self.user.username

    @property
    def upcoming_appointments(self):
        from django.utils import timezone
        return self.appointment_set.filter(
            appointment_date__gte=timezone.now(),
            status='scheduled'
        ).order_by('appointment_date')
