from django.urls import path
from .views import home, about, services, dashboard

app_name = 'pages'

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('dashboard/', dashboard, name='dashboard'),
]
