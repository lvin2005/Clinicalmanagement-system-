from django.db import models
from patients.models import Patient
from doctors.models import Doctor

class MedicalRecord(models.Model):
    RECORD_TYPE_CHOICES = [
        ('diagnosis', 'Diagnosis'),
        ('treatment', 'Treatment'),
        ('lab_result', 'Lab Result'),
        ('imaging', 'Imaging'),
        ('prescription', 'Prescription'),
        ('vaccination', 'Vaccination'),
        ('allergy', 'Allergy'),
        ('surgery', 'Surgery'),
        ('discharge', 'Discharge Summary'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    record_type = models.CharField(max_length=20, choices=RECORD_TYPE_CHOICES)
    title = models.CharField(max_length=200)
    description = models.TextField()
    diagnosis = models.TextField(blank=True)
    treatment = models.TextField(blank=True)
    prescription = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    record_date = models.DateTimeField()
    is_confidential = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient.full_name} - {self.title} ({self.record_date.strftime('%Y-%m-%d')})"

class MedicalFile(models.Model):
    medical_record = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='medical_files/%Y/%m/')
    filename = models.CharField(max_length=255)
    file_type = models.CharField(max_length=50)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey('doctors.Doctor', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.filename} - {self.medical_record}"

    @property
    def file_size(self):
        size = self.file.size
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024.0:
                return f"{size:.1f} {unit}"
            size /= 1024.0
        return f"{size:.1f} TB"
