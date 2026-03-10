from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Patient
from .forms import PatientForm

def patient_list(request):
    query = request.GET.get('q', '')
    patients = Patient.objects.all()
    
    if query:
        patients = patients.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(phone__icontains=query) |
            Q(email__icontains=query)
        )
    
    context = {
        'patients': patients,
        'query': query,
    }
    return render(request, 'patients/patient_list.html', context)

def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    appointments = patient.appointment_set.all().order_by('-appointment_date')
    medical_records = patient.medicalrecord_set.all().order_by('-created_at')
    
    context = {
        'patient': patient,
        'appointments': appointments,
        'medical_records': medical_records,
    }
    return render(request, 'patients/patient_detail.html', context)

@login_required
def create_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save()
            messages.success(request, f'Patient {patient.full_name} has been created successfully.')
            return redirect('patients:detail', pk=patient.pk)
    else:
        form = PatientForm()
    
    return render(request, 'patients/create_patient.html', {'form': form})

@login_required
def update_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            patient = form.save()
            messages.success(request, f'Patient {patient.full_name} has been updated successfully.')
            return redirect('patients:detail', pk=patient.pk)
    else:
        form = PatientForm(instance=patient)
    
    return render(request, 'patients/update_patient.html', {'form': form, 'patient': patient})

@login_required
def delete_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    
    if request.method == 'POST':
        name = patient.full_name
        patient.delete()
        messages.success(request, f'Patient {name} has been deleted successfully.')
        return redirect('patients:list')
    
    return render(request, 'patients/delete_patient.html', {'patient': patient})
