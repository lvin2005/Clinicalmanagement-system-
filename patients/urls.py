from django.urls import path
from . import views

app_name = 'patients'

urlpatterns = [
    path('', views.patient_list, name='list'),
    path('create/', views.create_patient, name='create'),
    path('<int:pk>/', views.patient_detail, name='detail'),
    path('<int:pk>/update/', views.update_patient, name='update'),
    path('<int:pk>/delete/', views.delete_patient, name='delete'),
]
