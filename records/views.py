from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import MedicalRecord, MedicalFile
from patients.models import Patient
from doctors.models import Doctor

def medical_record_list(request):
    query = request.GET.get('q', '')
    patient_id = request.GET.get('patient', '')
    record_type = request.GET.get('type', '')
    
    records = MedicalRecord.objects.select_related('patient', 'doctor').all()
    
    if query:
        records = records.filter(
            Q(patient__first_name__icontains=query) |
            Q(patient__last_name__icontains=query) |
            Q(doctor__user__first_name__icontains=query) |
            Q(doctor__user__last_name__icontains=query) |
            Q(title__icontains=query) |
            Q(diagnosis__icontains=query)
        )
    
    if patient_id:
        records = records.filter(patient_id=patient_id)
    
    if record_type:
        records = records.filter(record_type=record_type)
    
    context = {
        'records': records.order_by('-record_date'),
        'query': query,
        'patient_id': patient_id,
        'record_type': record_type,
        'record_types': MedicalRecord.RECORD_TYPE_CHOICES,
        'patients': Patient.objects.all().order_by('last_name', 'first_name'),
    }
    return render(request, 'records/medical_record_list.html', context)

@login_required
def create_medical_record(request):
    if request.method == 'POST':
        # Handle form submission
        patient_id = request.POST.get('patient')
        doctor_id = request.POST.get('doctor')
        record_type = request.POST.get('record_type')
        title = request.POST.get('title')
        description = request.POST.get('description')
        diagnosis = request.POST.get('diagnosis', '')
        treatment = request.POST.get('treatment', '')
        prescription = request.POST.get('prescription', '')
        notes = request.POST.get('notes', '')
        record_date = request.POST.get('record_date')
        is_confidential = request.POST.get('is_confidential') == 'on'
        
        try:
            patient = Patient.objects.get(id=patient_id)
            doctor = Doctor.objects.get(id=doctor_id)
            
            record = MedicalRecord.objects.create(
                patient=patient,
                doctor=doctor,
                record_type=record_type,
                title=title,
                description=description,
                diagnosis=diagnosis,
                treatment=treatment,
                prescription=prescription,
                notes=notes,
                record_date=record_date,
                is_confidential=is_confidential
            )
            
            messages.success(request, f'Medical record "{title}" has been created successfully.')
            return redirect('records:detail', pk=record.pk)
            
        except (Patient.DoesNotExist, Doctor.DoesNotExist) as e:
            messages.error(request, 'Invalid patient or doctor selected.')
        except Exception as e:
            messages.error(request, f'Error creating medical record: {str(e)}')
    
    patients = Patient.objects.all().order_by('last_name', 'first_name')
    doctors = Doctor.objects.select_related('user').all().order_by('user__last_name', 'user__first_name')
    
    context = {
        'patients': patients,
        'doctors': doctors,
        'record_types': MedicalRecord.RECORD_TYPE_CHOICES,
    }
    return render(request, 'records/create_medical_record.html', context)

def medical_record_detail(request, pk):
    record = get_object_or_404(MedicalRecord.objects.select_related('patient', 'doctor'), pk=pk)
    files = record.files.all()
    
    context = {
        'record': record,
        'files': files,
    }
    return render(request, 'records/medical_record_detail.html', context)

@login_required
def patient_records(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    records = patient.medicalrecord_set.select_related('doctor').order_by('-record_date')
    
    context = {
        'patient': patient,
        'records': records,
    }
    return render(request, 'records/patient_records.html', context)
