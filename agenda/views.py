from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CitaForm
from .models import Cita, Horario, Servicio
from datetime import time
from django.http import JsonResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


#--------------------------------------------------------


def reservar(request):
    return render(request, 'agenda/agendar.html')


#--------------------------------------------------------

def horarios_disponibles(request):
    fecha = request.GET.get('fecha')

    if not fecha:
        return JsonResponse({'horarios': []})

    # Obtener horarios desde la base de datos (ADMIN)
    horarios = Horario.objects.all().order_by('hora')
    HORARIOS = [h.hora.strftime("%H:%M") for h in horarios]

    # Obtener horarios ya reservados ese día
    citas = Cita.objects.filter(fecha=fecha).values_list('hora__hora', flat=True)
    ocupados = [c.strftime("%H:%M") for c in citas]

    # Crear lista de horarios disponibles
    disponibles = [h for h in HORARIOS if h not in ocupados]

    return JsonResponse({'horarios': disponibles})


#--------------------------------------------------------

def home(request):
    servicios = Servicio.objects.all()
    return render(request, "agenda/home.html", {"servicios": servicios})

#--------------------------------------------------------

def lista_servicios(request):
    return HttpResponse("<h1>Lista de servicios</h1>")

#--------------------------------------------------------


def lista_horarios(request):
    return HttpResponse("<h1>Horarios disponibles</h1>")

#--------------------------------------------------------


def agendar_cita(request):
    if request.method == 'POST':
        data = request.POST.copy()

        hora_seleccionada = data.get("hora")

        try:
            hora_obj = Horario.objects.get(hora=hora_seleccionada)
        except Horario.DoesNotExist:
            messages.error(request, "La hora seleccionada no existe.")
            return redirect('agendar_cita')

        data["hora"] = hora_obj.id
        form = CitaForm(data)

        if form.is_valid():
            cita = form.save()

            send_mail(
                subject='📅 Nueva cita agendada',
                message=f"""
Se ha agendado una nueva cita:

Nombre: {cita.nombre_cliente}
Teléfono: {cita.telefono}
Servicio: {cita.servicio}
Fecha: {cita.fecha}
Hora: {cita.hora}
""",
                from_email=None,
                recipient_list=['benjajamin17@gmail.com'],
                fail_silently=False,
            )

            messages.success(request, "¡Tu cita fue reservada con éxito! 😎✂️")
            return redirect('home')

        else:
            messages.error(request, "Formulario inválido.")

    else:
        form = CitaForm()

    return render(request, "agenda/agendar.html", {"form": form})
