from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from patients.models import Patient
from appointments.models import Appointment
from records.models import MedicalRecord
from doctors.models import Doctor
from django.utils import timezone
from django.db.models import Count

def home(request):
    if request.user.is_authenticated:
        return redirect('pages:dashboard')
    
    # Public homepage - redirect to login
    return redirect('accounts:login')

def about(request):
    return render(request, 'pages/about.html')

def services(request):
    return render(request, 'pages/services.html')

@login_required
def dashboard(request):
    # Check if user is a doctor
    try:
        profile = request.user.userprofile
        is_doctor = profile.user_type == 'doctor'
    except:
        is_doctor = False
    
    if is_doctor:
        # Doctor-specific data - simplified since we don't have doctor relationship yet
        upcoming_appointments = Appointment.objects.filter(
            appointment_date__gte=timezone.now(),
            status='scheduled'
        ).order_by('appointment_date')[:10]
        today_appointments = Appointment.objects.filter(
            appointment_date__date=timezone.now().date(),
            status='scheduled'
        ).order_by('appointment_date')
        recent_records = MedicalRecord.objects.order_by('-created_at')[:5]
    else:
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
