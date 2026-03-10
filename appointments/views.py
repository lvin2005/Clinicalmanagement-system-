from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from .models import Appointment
from patients.models import Patient
from doctors.models import Doctor
from .forms import AppointmentForm

def appointment_list(request):
    query = request.GET.get('q', '')
    status_filter = request.GET.get('status', '')
    date_filter = request.GET.get('date', '')
    
    appointments = Appointment.objects.select_related('patient', 'doctor').all()
    
    if query:
        appointments = appointments.filter(
            Q(patient__first_name__icontains=query) |
            Q(patient__last_name__icontains=query) |
            Q(doctor__user__first_name__icontains=query) |
            Q(doctor__user__last_name__icontains=query)
        )
    
    if status_filter:
        appointments = appointments.filter(status=status_filter)
    
    if date_filter:
        today = timezone.now().date()
        if date_filter == 'today':
            appointments = appointments.filter(appointment_date__date=today)
        elif date_filter == 'upcoming':
            appointments = appointments.filter(appointment_date__date__gt=today)
        elif date_filter == 'past':
            appointments = appointments.filter(appointment_date__date__lt=today)
    
    context = {
        'appointments': appointments.order_by('-appointment_date'),
        'query': query,
        'status_filter': status_filter,
        'date_filter': date_filter,
        'status_choices': Appointment.STATUS_CHOICES,
    }
    return render(request, 'appointments/appointment_list.html', context)

@login_required
def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            messages.success(request, f'Appointment for {appointment.patient.full_name} has been scheduled successfully.')
            return redirect('appointments:detail', pk=appointment.pk)
    else:
        form = AppointmentForm()
    
    return render(request, 'appointments/create_appointment.html', {'form': form})

def appointment_detail(request, pk):
    appointment = get_object_or_404(Appointment.objects.select_related('patient', 'doctor'), pk=pk)
    
    context = {
        'appointment': appointment,
    }
    return render(request, 'appointments/appointment_detail.html', context)

@login_required
def update_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            appointment = form.save()
            messages.success(request, f'Appointment for {appointment.patient.full_name} has been updated successfully.')
            return redirect('appointments:detail', pk=appointment.pk)
    else:
        form = AppointmentForm(instance=appointment)
    
    return render(request, 'appointments/update_appointment.html', {'form': form, 'appointment': appointment})

@login_required
def cancel_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    
    if request.method == 'POST':
        appointment.status = 'cancelled'
        appointment.save()
        messages.success(request, f'Appointment for {appointment.patient.full_name} has been cancelled.')
        return redirect('appointments:detail', pk=appointment.pk)
    
    return render(request, 'appointments/cancel_appointment.html', {'appointment': appointment})
