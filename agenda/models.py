from django.db import models

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre

class Horario(models.Model):
    hora = models.TimeField(unique=True)

    def __str__(self):
        return self.hora.strftime("%H:%M")

class Cita(models.Model):
    nombre_cliente = models.CharField(max_length=120)
    telefono = models.CharField(max_length=20)
    fecha = models.DateField()
    hora = models.ForeignKey(Horario, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre_cliente} - {self.fecha} {self.hora}"