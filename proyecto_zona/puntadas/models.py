from django.db import models
from django.utils import timezone
from django.contrib import admin


class Puntada(models.Model):
    descripcion=models.TextField()
    costo_puntada=models.FloatField()
    status=models.IntegerField()
    fecha_publicacion=models.DateTimeField(
    default=timezone.now)

    def __str__(self):
        return self.descripcion

class Empleado(models.Model):
    nombre=models.CharField(max_length=200)
    email=models.EmailField(max_length=254)
    fecha_nacimiento=models.DateTimeField()
    puntadas=models.ManyToManyField(Puntada,through='Registro')

    def __str__(self):
        return self.nombre


class Registro(models.Model):
    puntada=models.ForeignKey(Puntada,on_delete=models.CASCADE)
    empleado=models.ForeignKey(Empleado,on_delete=models.CASCADE)

class RegistroInLine(admin.TabularInline):
    model=Registro
    extra=1

class PuntadaAdmin(admin.ModelAdmin):
    inlines=(RegistroInLine,)

class EmpleadoAdmin(admin.ModelAdmin):
    inlines=(RegistroInLine,)
