from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CitaForm

def inicio(request):
    return render(request, 'agenda/inicio.html')

def lista_servicios(request):
    return HttpResponse("<h1>Lista de servicios</h1>")

def lista_horarios(request):
    return HttpResponse("<h1>Horarios disponibles</h1>")

def agendar_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'agenda/exito.html')  # página de confirmación
    else:
        form = CitaForm()
    
    return render(request, 'agenda/agendar.html', {'form': form})