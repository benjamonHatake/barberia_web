from django.http import HttpResponse

def inicio(request):
    return HttpResponse("<h1>Página de inicio Barbería</h1>")

def lista_servicios(request):
    return HttpResponse("<h1>Lista de servicios</h1>")

def lista_horarios(request):
    return HttpResponse("<h1>Horarios disponibles</h1>")

def agendar_cita(request):
    return HttpResponse("<h1>Formulario para agendar cita</h1>")
