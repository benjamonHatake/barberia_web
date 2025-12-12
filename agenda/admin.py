from django.contrib import admin
from .models import Servicio, Horario, Cita

admin.site.register(Servicio)
admin.site.register(Horario)
admin.site.register(Cita)
