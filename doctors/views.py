from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from .models import Doctor

def doctor_list(request):
    query = request.GET.get('q', '')
    specialization = request.GET.get('specialization', '')
    
    doctors = Doctor.objects.select_related('user').all()
    
    if query:
        doctors = doctors.filter(
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query) |
            Q(specialization__icontains=query)
        )
    
    if specialization:
        doctors = doctors.filter(specialization=specialization)
    
    specializations = Doctor.SPECIALIZATION_CHOICES
    
    context = {
        'doctors': doctors,
        'query': query,
        'specializations': specializations,
        'selected_specialization': specialization,
    }
    return render(request, 'doctors/doctor_list.html', context)

def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctor.objects.select_related('user'), pk=pk)
    upcoming_appointments = doctor.upcoming_appointments[:5]
    
    context = {
        'doctor': doctor,
        'upcoming_appointments': upcoming_appointments,
    }
    return render(request, 'doctors/doctor_detail.html', context)

@login_required
def doctor_dashboard(request):
    try:
        doctor = request.user.doctor
    except Doctor.DoesNotExist:
        messages.error(request, 'You are not registered as a doctor.')
        return redirect('pages:home')
    
    upcoming_appointments = doctor.upcoming_appointments
    today_appointments = doctor.appointment_set.filter(
        appointment_date__date=timezone.now().date(),
        status='scheduled'
    ).order_by('appointment_date')
    
    context = {
        'doctor': doctor,
        'upcoming_appointments': upcoming_appointments,
        'today_appointments': today_appointments,
    }
    return render(request, 'doctors/dashboard.html', context)
