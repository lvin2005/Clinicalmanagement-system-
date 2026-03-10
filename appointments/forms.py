from django import forms
from .models import Appointment
from patients.models import Patient
from doctors.models import Doctor

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            'patient', 'doctor', 'appointment_date', 'appointment_type', 'reason',
            'notes', 'symptoms', 'blood_pressure', 'heart_rate', 'temperature',
            'weight', 'height', 'prescription', 'follow_up_date'
        ]
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control'}),
            'doctor': forms.Select(attrs={'class': 'form-control'}),
            'appointment_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'appointment_type': forms.Select(attrs={'class': 'form-control'}),
            'reason': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'symptoms': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'blood_pressure': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '120/80'}),
            'heart_rate': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '72'}),
            'temperature': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'placeholder': '98.6'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'placeholder': '150.0'}),
            'height': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'placeholder': '5.10'}),
            'prescription': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'follow_up_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['patient'].queryset = Patient.objects.all().order_by('last_name', 'first_name')
        self.fields['doctor'].queryset = Doctor.objects.select_related('user').all().order_by('user__last_name', 'user__first_name')
