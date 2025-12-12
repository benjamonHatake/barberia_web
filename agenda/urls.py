from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('servicios/', views.lista_servicios, name='lista_servicios'),
    path('horarios/', views.lista_horarios, name='lista_horarios'),
    path('agendar/', views.agendar_cita, name='agendar_cita'),
    path('horarios-disponibles/', views.horarios_disponibles, name='horarios_disponibles'),
    path('reservar/', views.reservar, name='reservar'),

    path("api/horas-disponibles/", views.horarios_disponibles, name="horas_disponibles"),
]
