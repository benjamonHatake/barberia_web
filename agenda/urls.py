from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('servicios/', views.lista_servicios, name='lista_servicios'),
    path('horarios/', views.lista_horarios, name='lista_horarios'),
    path('agendar/', views.agendar_cita, name='agendar_cita'),
]
