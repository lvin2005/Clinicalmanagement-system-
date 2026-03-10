from django.urls import path
from . import views

app_name = 'records'

urlpatterns = [
    path('', views.medical_record_list, name='list'),
    path('create/', views.create_medical_record, name='create'),
    path('<int:pk>/', views.medical_record_detail, name='detail'),
    path('patient/<int:patient_id>/', views.patient_records, name='patient_records'),
]
