from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from patients.models import Patient
from appointments.models import Appointment
from records.models import MedicalRecord
from doctors.models import Doctor
from django.utils import timezone
from django.db.models import Count

def home(request):
    # Get statistics for dashboard
    total_patients = Patient.objects.count()
    total_doctors = Doctor.objects.count()
    total_appointments = Appointment.objects.count()
    
    # Get recent data
    recent_patients = Patient.objects.order_by('-created_at')[:5]
    upcoming_appointments = Appointment.objects.filter(
        appointment_date__gte=timezone.now(),
        status='scheduled'
    ).order_by('appointment_date')[:5]
    
    context = {
        'total_patients': total_patients,
        'total_doctors': total_doctors,
        'total_appointments': total_appointments,
        'recent_patients': recent_patients,
        'upcoming_appointments': upcoming_appointments,
    }
    return render(request, 'pages/home.html', context)

def about(request):
    return render(request, 'pages/about.html')

def services(request):
    return render(request, 'pages/services.html')

@login_required
def dashboard(request):
    # Check if user is a doctor
    try:
        doctor = request.user.doctor
        is_doctor = True
        # Doctor-specific data
        upcoming_appointments = doctor.upcoming_appointments
        today_appointments = doctor.appointment_set.filter(
            appointment_date__date=timezone.now().date(),
            status='scheduled'
        ).order_by('appointment_date')
        recent_records = MedicalRecord.objects.filter(doctor=doctor).order_by('-created_at')[:5]
    except Doctor.DoesNotExist:
        is_doctor = False
        # Staff/admin data
        upcoming_appointments = Appointment.objects.filter(
            appointment_date__gte=timezone.now(),
            status='scheduled'
        ).order_by('appointment_date')[:10]
        today_appointments = Appointment.objects.filter(
            appointment_date__date=timezone.now().date(),
            status='scheduled'
        ).order_by('appointment_date')
        recent_records = MedicalRecord.objects.order_by('-created_at')[:5]
    
    # General statistics
    total_patients = Patient.objects.count()
    total_appointments_today = Appointment.objects.filter(
        appointment_date__date=timezone.now().date()
    ).count()
    
    # Recent activity
    recent_patients = Patient.objects.order_by('-created_at')[:5]
    
    context = {
        'is_doctor': is_doctor,
        'total_patients': total_patients,
        'total_appointments_today': total_appointments_today,
        'upcoming_appointments': upcoming_appointments,
        'today_appointments': today_appointments,
        'recent_records': recent_records,
        'recent_patients': recent_patients,
    }
    return render(request, 'pages/dashboard.html', context)
