from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    USER_TYPE_CHOICES = [
        ('staff', 'Staff Member'),
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
        ('admin', 'Administrator'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='staff')
    phone = models.CharField(max_length=20, blank=True)
    department = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username} - {self.get_user_type_display()}"

    @property
    def is_doctor(self):
        return self.user_type == 'doctor'

    @property
    def is_staff_member(self):
        return self.user_type in ['staff', 'admin']
