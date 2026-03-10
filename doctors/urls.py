from django.urls import path
from . import views

app_name = 'doctors'

urlpatterns = [
    path('', views.doctor_list, name='list'),
    path('<int:pk>/', views.doctor_detail, name='detail'),
    path('dashboard/', views.doctor_dashboard, name='dashboard'),
]
